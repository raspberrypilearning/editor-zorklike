<h2 class="c-project-heading--task">Collect random items</h2>
--- task ---

In `game.py`, keep the `get [item]` command so the player can collect whatever random item appears.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: game.py
line_numbers: true
line_highlights: 44-51
---
elif command == 'get':
    if 'item' in rooms[current_room] and rooms[current_room]['item'] == target:
        inventory.append(target)
        print('You picked up the ' + target)
        del rooms[current_room]['item']
    else:
        print('There is no ' + target + ' here!')
--- /code ---
</div>

--- task ---

Click **Run**, type `get` followed by the exact item name shown.

The item is added to inventory and removed from the room.

--- /task ---
