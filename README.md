# IT140_python_project

This project requires building a text-based adventure game in Python. You must navigate a map containing at least eight distinct rooms, collect six unique items, and either win by collecting all items or lose by entering the villain's room.

# cat and mouse adventure game

## game instructions
Collect all 6 items to make a gourmet, 4 cheese, grilled cheese sandwich and return to the Entry to "win the game"
or encounter Mr. Whiskers and become his afternoon snack.

[Storyboard and Map](https://github.com/cepetrush/IT140_python_project/blob/f30a84bc7a374fcac740447b5feef4af82cfb2c0/documents/Storyboard.md)


## core project requirements
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
