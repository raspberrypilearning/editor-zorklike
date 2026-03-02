<h2 class="c-project-heading--task">Build the map layout</h2>
--- task ---

In `main.py`, replace the highlighted `rooms` block with this map layout.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_highlights: 42-56
---
rooms = {
    start_room: {
        'south': monster_room,  # Path to the monster room.
        'east': treasure_room,  # Path to the treasure room.
    },
    monster_room: {
        'north': start_room,  # Path back to the start room.
    },
    treasure_room: {
        'west': start_room,  # Path back to the start room.
        'south': goal_room,  # Path to the goal room.
    },
    goal_room: {
        'north': treasure_room,  # Path back to the treasure room.
    },
}
--- /code ---
</div>

--- task ---

Click **Run**.

Look for scripted command lines in the output such as `> go east`, `> go west`, and `> go south`.

You can move through all connected rooms without code errors.

--- /task ---
