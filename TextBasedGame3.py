#Project 2 Text Based Game
#Christine Petrush

#prints out instructions for the game
def show_instructions():
    print("Cat amd Mouse Adventure Game")
    print("\nCollect all 6 items to make a gourmet, 4 cheese, grilled cheese sandwich and return to the Entry to"
          " win the game")
    print("Or encounter Mr. Whiskers and become his afternoon snack!")
    print("\nMove commands: go South, go North, go East, go West")
    print("Add to inventory: get 'Item name'")

#show player's status
def show_status(current_room, inventory, room):
    print("\nYou are in the {}".format(current_room))
    print("Your current inventory is: ", inventory)
    if 'item' in room.keys():
        if room['item'] not in inventory:
            print('You see,', room['item'])
    print('--------------------------------')

#data setup
def main():
    inventory = []
    rooms = {
        'Grand Ballroom': {'south': 'Entry', 'north': 'Kitchen', 'east': 'Study', 'west': 'Dining Room', 'item': 'Gouda'},
        'Entry': {'north': 'Grand Ballroom', 'east': 'Cellar'},
        'Cellar': {'west': 'Entry', 'item': 'Cheddar'},
        'Study': {'west': 'Grand Ballroom', 'north': 'Bedroom', 'item': 'Swiss'},
        'Bedroom': {'south': 'Study', 'item': 'Brie'},
        'Dining Room': {'east': 'Grand Ballroom', 'item': 'Mr. Whiskers!'},
        'Kitchen': {'south': 'Grand Ballroom', 'east': 'Pantry', 'item': 'Butter'},
        'Pantry': {'west': 'Kitchen', 'item': 'Bread'}
        }
    current_room = rooms['Entry']
    c_room_name = 'Entry'
    directions = ['north', 'south', 'east', 'west']

    show_instructions()

    #game loop
    while True:
        show_status(c_room_name, inventory, current_room)
        # winning the game
        if c_room_name == 'Entry':
            if len(inventory) == 6:
                print('\nCongratulations! You have gathered all the needed ingredients while avoiding Mr. Whiskers.')
                print('Enjoy your gourmet, 4 cheese, grilled cheese sandwich.')
                print('You have won the game! Thank you for playing!')
                break
        #losing the game
        if c_room_name == 'Dining Room':
            print("He pounces and gobbles you up in one bite!")
            print('Munch, munch...Time for a cat nap...zzzz...Game Over!')
            print('Thank you for playing!  Better luck next time!')
            break

        player_move = input('Enter your move: ').strip().lower()

        #movement
        if len(player_move.split(' ')) > 0:
            action = player_move.split(' ')[0]
        if len(player_move.split(' ')) > 1:
            command = player_move.split(' ')[1]
            print('You entered: ', player_move)
        if action == 'go':
            if command in directions:
                if command in current_room:
                    c_room_name = current_room[command]
                    current_room = rooms[current_room[command]]
                else:
                    print("You can't go that way.")
            else:
                print('Invalid Input!')

        #inventory
        elif action == 'get':
            if current_room['item'].lower() == command:
                if current_room['item'] in inventory:
                    print('You already have that item')
                else:
                    inventory.append(current_room['item'])
                    print(current_room['item'], 'added to your inventory')
            else:
                print("Can't get item")
        else:
            print('Invalid Input!')

main()


