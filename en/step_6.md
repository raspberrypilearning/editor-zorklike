<h2 class="c-project-heading--task">Add random items to collect</h2>
--- task ---

In `main.py`, add the two `'item'` lines in the highlighted places inside the existing `rooms` block:

+ `item_one` in the start room
+ `item_two` in the treasure room

Do not replace the whole dictionary. Add only the two highlighted `'item'` lines.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_highlights: 46, 53
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
--- /code ---
</div>

--- task ---

Click **Run**.

Look for scripted `get` lines in the output, for example `> get ...`.

The item is added to inventory and removed from the room.

--- /task ---
