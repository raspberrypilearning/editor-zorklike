<h2 class="c-project-heading--task">Build the random map</h2>
--- task ---

Use your generated names to create the `rooms` dictionary.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_highlights: 25-41
---
rooms = {
    start_room: {
        'south': monster_room,
        'east': treasure_room,
        'item': item_one,
    },
    monster_room: {
        'north': start_room,
        'item': monster_name,
    },
    treasure_room: {
        'west': start_room,
        'south': goal_room,
        'item': item_two,
    },
    goal_room: {
        'north': treasure_room,
    },
}
--- /code ---
</div>

--- task ---

Click **Run** and try moving around using `go south`, `go east`, and `go west`.

**Stable point:** Navigation works with the new random room names.

--- /task ---
