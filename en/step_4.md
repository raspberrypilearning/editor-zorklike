<h2 class="c-project-heading--task">Generate unique names for one adventure</h2>
--- task ---

Add a helper function to make several unique random phrases, then assign them to rooms and items.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_highlights: 11-23
---
def unique_phrases(count):
    phrases = set()
    while len(phrases) < count:
        phrases.add(random_phrase())
    return list(phrases)


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

--- task ---

Click **Run**.

**Stable point:** The room and item variables are always filled, and they change each run.

--- /task ---
