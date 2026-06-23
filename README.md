# IT140_python_project

## Core Project Requirements
The Python script must execute the following functions:
- **The Map**
  - Built using a nested dictionary where keys represent rooms, and values represent directions and item locations.
- **Starting Room**
  - The player must spawn in a disignated starting room that contains zero items.
- **Villain's Room**
  - One room must house the villain and contain zero items.
- **Input Validation**
  - Code must handle directional commands (e.g., go North, East) and collection commands (e.g., get 'item name').
- **Inventory Tracking**
  - A dynamically updating list that stores collected items.
- **Win/Loss Conditions**
  - Moving into the villain's room triggers a conditional check
    - 6 items in inventory = win
    - fewer than 6 items = game over
