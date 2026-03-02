<h2 class="c-project-heading--task">Add a random win condition</h2>
--- task ---

In `main.py`, create `required_items` and pass it into `run_game`.

Then, in `game.py`, check that the player is in the goal room with all required items.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_highlights: 44-55
---
inventory = []
current_room = start_room
required_items = [item_one, item_two]

current_room, inventory = run_game(
    current_room,
    inventory,
    rooms,
    goal_room,
    required_items,
    monster_name,
)
--- /code ---
</div>

<div class="c-project-code">
--- code ---
---
language: python
filename: game.py
line_numbers: true
line_highlights: 60-62
---
if current_room == goal_room and all(item in inventory for item in required_items):
    print('You completed the quest... YOU WIN!')
    break
--- /code ---
</div>

--- task ---

Click **Run** and win one full game.

**Stable point:** You can finish the game only after collecting both random items.

--- /task ---
