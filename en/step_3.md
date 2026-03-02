<h2 class="c-project-heading--task">Pick random two-word names</h2>
--- task ---

In `game.py`, add a helper function that returns a random adjective + noun phrase.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: game.py
line_numbers: true
line_highlights: 1, 4-5
---
import random


def random_phrase(adjectives, nouns):
    return random.choice(adjectives) + ' ' + random.choice(nouns)
--- /code ---
</div>

--- task ---

To test, temporarily import and print one phrase in `main.py`:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_highlights: 1, 4
---
from game import run_game, random_phrase
from word_lists import adjectives, nouns

print(random_phrase(adjectives, nouns))
--- /code ---
</div>

Click **Run** a few times.

You see a different two-word phrase between runs.

--- /task ---
