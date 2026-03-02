<h2 class="c-project-heading--task">Add The Monster Room</h2>
--- task ---
Add the monster item to `monster_room` and set a short scripted test path into that room.
--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 42
line_highlights: 44,47-49
---
    monster_room: {
        'north': start_room,
        'item': monster_name,  # Entering this room now causes game over.
    },

scripted_moves = [
    'go south',
]
--- /code ---
</div>

--- task ---
**Test:** Click **Run**.

The output ends with the monster game-over message.
--- /task ---
