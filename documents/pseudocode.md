**Pseudocode to “Move Between Rooms”**

FUNCTION show instructions  
	&emsp;&emsp;DISPLAY name of game  
	&emsp;&emsp;DISPLAY basic rules of game  
	&emsp;&emsp;DISPLAY move commands (‘go North’, ‘go South’, ‘go East’, ‘go West’)  
	&emsp;&emsp;DISPLAY get item command (get ‘item name’)  
END FUNCTION  
FUNCTION show status (current room, inventory, rooms)  
	&emsp;&emsp;DISPLAY current room of player (‘You are in the {}’.format (current room))  
	&emsp;&emsp;DISPLAY current inventory  
	&emsp;&emsp;DISPLAY item in room they are currently in if one exists  
END FUNCTION  
FUNCTION main  
	&emsp;&emsp;SET dictionary (linking a room to other rooms and items)  
		&emsp;&emsp;&emsp;&emsp;room \= ‘Grand Ballroom’: {‘South’: ‘Entry’, ‘North’: ‘Kitchen’, ‘East’: ‘Study’, ‘West’: ‘Dining Room’, ‘Item’: ‘Gouda’}  
		&emsp;&emsp;&emsp;&emsp;‘Entry’: {‘North’: ‘Grand Ballroom’, ‘East’: ‘Cellar’}  
		&emsp;&emsp;&emsp;&emsp;‘Cellar’: {‘West’: ‘Entry’, ‘Item’: ‘Cheddar’}  
		&emsp;&emsp;&emsp;&emsp;‘Study’: {‘West’: ‘Grand Ballroom’, ‘North’: ‘Bedroom’, ‘Item’: ‘Swiss’}  
		&emsp;&emsp;&emsp;&emsp;‘Bedroom’ {‘South’: ‘Study’, ‘Item’: ‘Brie’}  
		&emsp;&emsp;&emsp;&emsp;‘Dining Room’: {‘East’: ‘Grand Ballroom’, ‘Item’: ‘Mr. Whiskers’}  
		&emsp;&emsp;&emsp;&emsp;‘Kitchen’ {‘South’: ‘Grand Ballroom’, ‘East’: ‘Pantry’, ‘Item’: ‘Butter’}  
		&emsp;&emsp;&emsp;&emsp;‘Pantry’: {‘West’: ‘Kitchen’, ‘Item’: ‘Italian Bread’}  
	&emsp;&emsp;SET variable directions \= ‘North’, ‘South’, ‘East’, ‘West’  
	&emsp;&emsp;SET variable current room \= rooms \[‘Entry’\]  
	&emsp;&emsp;SET variable inventory \= \[\]  
END FUNCTION  
CALL show instructions function  
WHILE True  
	&emsp;&emsp;CALL show status function  
	&emsp;&emsp;INPUT player move (‘Enter your move:’)  
	&emsp;&emsp;SET variable action \= split(player move, ‘’)\[0\]  
	&emsp;&emsp;SET variable location \= split(player move, ‘’)\[1\]  
		&emsp;&emsp;&emsp;&emsp;IF action \== ‘go’ THEN  
			&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;IF location in directions THEN  
			&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;IF location in current room THEN  
					&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;current room \= rooms\[current room\[player move\]\]  
				&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;ELSE  
					&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;DISPLAY ‘You can’t go that way’  
				&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;ENDIF  
			&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;ELSE  
				&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;DISPLAY ‘Invalid Input\!’  
			&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;ENDIF  
		&emsp;&emsp;&emsp;&emsp;ELSE  
			&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;DISPLAY ‘Invalid Input\!’  
		&emsp;&emsp;&emsp;&emsp;ENDIF  
ENDWHILE 

**Pseudocode to “Get an Item”**

FUNCTION show instructions  
	&emsp;&emsp;DISPLAY name of game  
	&emsp;&emsp;DISPLAY basic rules of game  
	&emsp;&emsp;DISPLAY move commands (‘go North’, ‘go South’, ‘go East’, ‘go West’)  
	&emsp;&emsp;DISPLAY get item command (get ‘item name’)  
END FUNCTION  
FUNCTION show status (current room, inventory, rooms)  
	&emsp;&emsp;DISPLAY current room of player (‘You are in the {}’.format (current room))  
	&emsp;&emsp;DISPLAY current inventory  
	&emsp;&emsp;DISPLAY item in room they are currently in if one exists  
END FUNCTION  
FUNCTION main  
	&emsp;&emsp;SET dictionary (linking a room to other rooms and items)  
		&emsp;&emsp;&emsp;&emsp;room \= ‘Grand Ballroom’: {‘South’: ‘Entry’, ‘North’: ‘Kitchen’, ‘East’: ‘Study’, ‘West’: ‘Dining Room’, ‘Item’: ‘Gouda’}  
		&emsp;&emsp;&emsp;&emsp;‘Entry’: {‘North’: ‘Grand Ballroom’, ‘East’: ‘Cellar’}  
		&emsp;&emsp;&emsp;&emsp;‘Cellar’: {‘West’: ‘Entry’, ‘Item’: ‘Cheddar’}  
		&emsp;&emsp;&emsp;&emsp;‘Study’: {‘West’: ‘Grand Ballroom’, ‘North’: ‘Bedroom’, ‘Item’: ‘Swiss’}  
		&emsp;&emsp;&emsp;&emsp;‘Bedroom’ {‘South’: ‘Study’, ‘Item’: ‘Brie’}  
		&emsp;&emsp;&emsp;&emsp;‘Dining Room’: {‘East’: ‘Grand Ballroom’, ‘Item’: ‘Mr. Whiskers’}  
		&emsp;&emsp;&emsp;&emsp;‘Kitchen’ {‘South’: ‘Grand Ballroom’, ‘East’: ‘Pantry’, ‘Item’: ‘Butter’}  
		&emsp;&emsp;&emsp;&emsp;‘Pantry’: {‘West’: ‘Kitchen’, ‘Item’: ‘Italian Bread’}  
	&emsp;&emsp;SET variable directions \= ‘North’, ‘South’, ‘East’, ‘West’  
	&emsp;&emsp;SET variable current room \= rooms \[‘Entry’\]  
	&emsp;&emsp;SET variable inventory \= \[\]  
END FUNCTION  
CALL show instructions function  
WHILE True  
	&emsp;&emsp;CALL show status function  
	&emsp;&emsp;INPUT command (‘Enter your move:’)  
	&emsp;&emsp;SET variable type \= split(command, ‘’)\[0\]  
	&emsp;&emsp;SET variable value \= split(command, ‘’)\[1\]  
		&emsp;&emsp;&emsp;&emsp;IF action \== ‘get’ THEN  
			&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;IF value in current room THEN  
			&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;inventory.append(current room\['Item'\])   
				&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;ELSE  
					&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;DISPLAY ‘Can't get item’  
				&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;ENDIF  
			&emsp;&emsp;&emsp;&emsp;ELSE  
				&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;DISPLAY ‘Invalid Input\!’  
			&emsp;&emsp;&emsp;&emsp;ENDIF  
ENDWHILE 


