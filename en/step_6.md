<h2 class="c-project-heading--task">Add Items To Collect</h2>
--- task ---
Add two random items to the map and update the scripted moves to collect them.
--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 38
line_highlights: 42,50,56-60
---
rooms = {
    start_room: {
        'south': monster_room,
        'east': treasure_room,
        'item': item_one,  # First item appears in the start room.
    },
    monster_room: {
        'north': start_room,
    },
    treasure_room: {
        'west': start_room,
        'south': goal_room,
        'item': item_two,  # Second item appears in the treasure room.
    },
    goal_room: {
        'north': treasure_room,
    },
}

scripted_moves = [
    'go east',
    f'get {item_two}',
    'go west',
    f'get {item_one}',
]
--- /code ---
</div>

--- task ---
**Test:** Click **Run**.

The output shows both `get` commands and both items being added to the inventory.
--- /task ---
