<h2 class="c-project-heading--task">Add a random phrase function</h2>
--- task ---

In `main.py`, add `import random` on the highlighted line.

Then add the `random_phrase()` function on the highlighted lines.

--- /task ---

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_highlights: 1, 20-21
---
import random
from game import run_game


def random_phrase():
    return random.choice(adjectives) + ' ' + random.choice(nouns)
--- /code ---
</div>

--- task ---

Add `print(random_phrase())` as a temporary line under your function to test.

Click **Run** a few times.

You see a different two-word phrase between runs.

--- /task ---
