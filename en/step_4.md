<h2 class="c-project-heading--task">Generate unique names for one adventure</h2>
--- task ---

In `game.py`, add a second helper to build a list of unique random phrases.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: game.py
line_numbers: true
line_highlights: 8-12
---
def unique_phrases(count, adjectives, nouns):
    phrases = set()
    while len(phrases) < count:
        phrases.add(random_phrase(adjectives, nouns))
    return list(phrases)
--- /code ---
</div>

--- task ---

In `main.py`, call that function:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_highlights: 1, 7
---
from game import run_game, unique_phrases
from word_lists import adjectives, nouns

names = unique_phrases(7, adjectives, nouns)
--- /code ---
</div>

Continue assigning names to rooms and items.

Click **Run**.

The room and item variables are always filled, and they change each run.

--- /task ---
