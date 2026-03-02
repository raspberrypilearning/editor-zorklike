<h2 class="c-project-heading--task">Build A Four-Room Map</h2>
--- task ---
Replace the `rooms` dictionary so the player can travel across four linked rooms.
--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 37
line_highlights: 40,41,44,47,48,51
---
# Step 5 builds this map into four connected rooms.
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
**Test:** Click **Run**.

The scripted movement output shows travel through more than two rooms.
--- /task ---
