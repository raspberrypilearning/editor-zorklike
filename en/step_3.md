<h2 class="c-project-heading--task">Pick random two-word names</h2>
--- task ---

In `main.py`, import `random` and create a function that returns a random adjective + noun phrase.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_highlights: 1, 7-8
---
import random

from game import run_game
from word_lists import adjectives, nouns


def random_phrase():
    return random.choice(adjectives) + ' ' + random.choice(nouns)
--- /code ---
</div>

--- task ---

Use `print(random_phrase())` once to test.

Click **Run** a few times.

**Stable point:** You see a different two-word phrase between runs.

--- /task ---
