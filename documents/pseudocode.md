**Pseudocode to “Move Between Rooms”**

FUNCTION show instructions  
	&emsp;DISPLAY name of game  
	DISPLAY basic rules of game  
	DISPLAY move commands (‘go North’, ‘go South’, ‘go East’, ‘go West’)  
	DISPLAY get item command (get ‘item name’)  
END FUNCTION  
FUNCTION show status (current room, inventory, rooms)  
	DISPLAY current room of player (‘You are in the {}’.format (current room))  
	DISPLAY current inventory  
	DISPLAY item in room they are currently in if one exists  
END FUNCTION  
FUNCTION main  
	SET dictionary (linking a room to other rooms and items)  
		room \= ‘Grand Ballroom’: {‘South’: ‘Entry’, ‘North’: ‘Kitchen’, ‘East’: ‘Study’, ‘West’: ‘Dining Room’, ‘Item’: ‘Gouda’}  
		‘Entry’: {‘North’: ‘Grand Ballroom’, ‘East’: ‘Cellar’}  
		‘Cellar’: {‘West’: ‘Entry’, ‘Item’: ‘Cheddar’}  
		‘Study’: {‘West’: ‘Grand Ballroom’, ‘North’: ‘Bedroom’, ‘Item’: ‘Swiss’}  
		‘Bedroom’ {‘South’: ‘Study’, ‘Item’: ‘Brie’}  
		‘Dining Room’: {‘East’: ‘Grand Ballroom’, ‘Item’: ‘Mr. Whiskers’}  
		‘Kitchen’ {‘South’: ‘Grand Ballroom’, ‘East’: ‘Pantry’, ‘Item’: ‘Butter’}  
		‘Pantry’: {‘West’: ‘Kitchen’, ‘Item’: ‘Italian Bread’}  
	SET variable directions \= ‘North’, ‘South’, ‘East’, ‘West’  
	SET variable current room \= rooms \[‘Entry’\]  
	SET variable inventory \= \[\]  
END FUNCTION  
CALL show instructions function  
WHILE True  
	CALL show status function  
	INPUT player move (‘Enter your move:’)  
	SET variable action \= split(player move, ‘’)\[0\]  
	SET variable location \= split(player move, ‘’)\[1\]  
		IF action \== ‘go’ THEN  
			IF location in directions THEN  
				IF location in current room THEN  
					current room \= rooms\[current room\[player move\]\]  
				ELSE  
					DISPLAY ‘You can’t go that way’  
				ENDIF  
			ELSE  
				DISPLAY ‘Invalid Input\!’  
			ENDIF  
		ELSE  
			DISPLAY ‘Invalid Input\!’  
		ENDIF  
ENDWHILE  
**Pseudocode to “Get an Item”**

FUNCTION show instructions  
	DISPLAY name of game  
	DISPLAY basic rules of game  
	DISPLAY move commands (‘go North’, ‘go South’, ‘go East’, ‘go West’)  
	DISPLAY get item command (get ‘item name’)  
END FUNCTION  
FUNCTION show status (current room, inventory, rooms)  
	DISPLAY current room of player (‘You are in the {}’.format (current room))  
	DISPLAY current inventory  
	DISPLAY item in room they are currently in if one exists  
END FUNCTION  
FUNCTION main  
	SET dictionary (linking a room to other rooms and items)  
		room \= ‘Grand Ballroom’: {‘South’: ‘Entry’, ‘North’: ‘Kitchen’, ‘East’: ‘Study’, ‘West’: ‘Dining             Room’, ‘Item’: ‘Gouda’}  
		‘Entry’: {‘North’: ‘Grand Ballroom’, ‘East’: ‘Cellar’}  
		‘Cellar’: {‘West’: ‘Entry’, ‘Item’: ‘Cheddar’}  
		‘Study’: {‘West’: ‘Grand Ballroom’, ‘North’: ‘Bedroom’, ‘Item’: ‘Swiss’}  
		‘Bedroom’ {‘South’: ‘Study’, ‘Item’: ‘Brie’}  
		‘Dining Room’: {‘East’: ‘Grand Ballroom’, ‘Item’: ‘Mr. Whiskers’}  
		‘Kitchen’ {‘South’: ‘Grand Ballroom’, ‘East’: ‘Pantry’, ‘Item’: ‘Butter’}  
		‘Pantry’: {‘West’: ‘Kitchen’, ‘Item’: ‘Italian Bread’}  
	SET variable directions \= ‘North’, ‘South’, ‘East’, ‘West’  
	SET variable current room \= rooms \[‘Entry’\]  
	SET variable inventory \= \[\]  
END FUNCTION  
CALL show instructions function  
WHILE True  
	CALL show status function  
	INPUT command (‘Enter your move:’)  
	SET variable type \= split(command, ‘’)\[0\]  
	SET variable value \= split(command, ‘’)\[1\]  
		IF type \== ‘get’ THEN  
			IF value in current room THEN  
			inventory.append(current room\[‘Item’\])  
			ELSE  
				DISPLAY ‘Can’t get item’’  
			ENDIF  
		ELSE  
			DISPLAY ‘Invalid Input\!’  
		ENDIF  
ENDWHILE

