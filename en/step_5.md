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
        'south': monster_room,
        'east': treasure_room,
    },
    monster_room: {
        'north': start_room,
    },
    treasure_room: {
        'west': start_room,
        'south': goal_room,
    },
    goal_room: {
        'north': treasure_room,
    },
}
--- /code ---
</div>

--- task ---

Click **Run**.

Look for scripted command lines in the output such as `> go east`, `> go west`, and `> go south`.

You can move through all connected rooms without code errors.

--- /task ---
