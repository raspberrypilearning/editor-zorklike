<h2 class="c-project-heading--task">Add a random monster loss condition</h2>
--- task ---

Use `monster_name` so the player loses if they enter the monster room.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: game.py
line_numbers: true
line_highlights: 56-58
---
if 'item' in rooms[current_room] and rooms[current_room]['item'] == monster_name:
    print('The ' + monster_name + ' catches you... GAME OVER!')
    break
--- /code ---
</div>

--- task ---

Click **Run** and move into the monster room.

**Stable point:** The game ends with a monster message.

--- /task ---
