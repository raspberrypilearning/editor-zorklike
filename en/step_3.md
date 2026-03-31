<h2 class="c-project-heading--task">Generate Random Room And Object Names</h2>
### Step 1
Replace the fixed names with generated room names and generated object names.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 24
line_highlights: 24-28,30-38
---
def unique_phrases(count, noun_list):
    phrases = set()  # A set keeps names unique.
    while len(phrases) < count:
        phrases.add(random_phrase(noun_list))  # Add random names until we have enough.
    return list(phrases)  # Convert back to a list for indexing.

room_names = unique_phrases(4, room_nouns)  # Create 4 unique room names.
object_names = unique_phrases(3, object_nouns)  # Create 3 unique object names.
start_room = room_names[0].title()  # Room where the player starts.
monster_room = room_names[1].title()  # Dangerous room.
treasure_room = room_names[2].title()  # Room with the second item.
goal_room = room_names[3].title()  # Room needed to win.
item_one = object_names[0]  # First item to collect.
item_two = object_names[1]  # Second item to collect.
monster_name = object_names[2]  # Random monster name.
--- /code ---
</div>

### Step 2
**Test:** Click **Run** two times.

The room and object names are different on each run.
