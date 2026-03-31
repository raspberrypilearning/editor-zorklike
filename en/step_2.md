<h2 class="c-project-heading--task">Add One Random Name Function</h2>
### Step 1
Add random word code so one adjective+noun name can be generated.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 1,29-30
---
import random
from game import run_game

# Step 2: edit these lists to match your story theme.
adjectives = [
    'chocolate',
    'golden',
    'fizzy',
    'sweet',
    'candy',
]

room_nouns = [
    'factory',
    'river',
    'elevator',
    'tunnel',
    'inventing room',
]

object_nouns = [
    'ticket',
    'gobstopper',
    'bar',
    'blueberry',
    'oompa loompa',
]


def random_phrase(noun_list):
    return random.choice(adjectives) + ' ' + random.choice(noun_list)
--- /code ---
</div>

### Step 2
**Test:** Add `print(random_phrase(room_nouns))` under the function and click **Run**.

You see a random two-word room-style name in the output.
