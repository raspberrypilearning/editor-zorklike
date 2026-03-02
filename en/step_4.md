<h2 class="c-project-heading--task">Generate random names for one game</h2>
--- task ---

In `main.py`, add this helper function on the highlighted lines.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_highlights: 24-28
---
def unique_phrases(count):
    phrases = set()  # A set keeps names unique.
    while len(phrases) < count:
        phrases.add(random_phrase())  # Add random names until we have enough.
    return list(phrases)  # Convert back to a list for indexing.
--- /code ---
</div>

--- task ---

Now replace the fixed room and item name lines with this generated-name block:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_highlights: 31-40
---
names = unique_phrases(7)  # Create 7 unique random names.
start_room = names[0].title()  # Room where the player starts.
monster_room = names[1].title()  # Dangerous room.
treasure_room = names[2].title()  # Room with the second item.
goal_room = names[3].title()  # Room needed to win.
item_one = names[4]  # First item to collect.
item_two = names[5]  # Second item to collect.
monster_name = names[6]  # Random monster name.
--- /code ---
</div>

Click **Run**.

The room and item variables are always filled, and they change each run.

--- /task ---
