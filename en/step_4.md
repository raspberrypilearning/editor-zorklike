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
    phrases = set()
    while len(phrases) < count:
        phrases.add(random_phrase())
    return list(phrases)
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
names = unique_phrases(7)
start_room = names[0].title()
monster_room = names[1].title()
treasure_room = names[2].title()
goal_room = names[3].title()
item_one = names[4]
item_two = names[5]
monster_name = names[6]
--- /code ---
</div>

Click **Run**.

The room and item variables are always filled, and they change each run.

--- /task ---
