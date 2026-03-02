<h2 class="c-project-heading--task">Add a random monster room</h2>
--- task ---

In `main.py`, in the highlighted `monster_room` block, add the `'item': monster_name` line.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_highlights: 50
---
monster_room: {
    'north': start_room,
    'item': monster_name,
},
--- /code ---
</div>

--- task ---

To test this with code only, temporarily replace your `scripted_moves` list with:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_highlights: 55-57
---
scripted_moves = [
    'go south',
]
--- /code ---
</div>

Click **Run** and you should see the game-over monster message.

After testing, put your longer `scripted_moves` list back for Step 8.

--- /task ---
