<h2 class="c-project-heading--task">Set The Win Condition</h2>
--- task ---
Set required items for winning and restore a scripted path that collects both items and reaches the goal room.
--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 50
line_highlights: 52,54-60
---
inventory = []
current_room = start_room
required_items = [item_one, item_two]  # Player must collect both to win.

scripted_moves = [
    'go east',
    f'get {item_two}',
    'go west',
    f'get {item_one}',
    'go east',
    'go south',
]
--- /code ---
</div>

--- task ---
**Test:** Click **Run**.

The output ends with the win message after both items are collected.
--- /task ---
