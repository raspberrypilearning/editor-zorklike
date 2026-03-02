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

# Step 3 and 4 will replace these fixed names with random names.
start_room = 'Chocolate Hall'
monster_room = 'Fizzy Tunnel'
treasure_room = 'Golden Inventing Room'
goal_room = 'Candy Elevator'
item_one = 'golden ticket'
item_two = 'everlasting gobstopper'
monster_name = 'giant blueberry'

# Step 5 builds this map into four connected rooms.
rooms = {
    start_room: {
        'south': monster_room,
    },
    monster_room: {
        'north': start_room,
    },
}

# Step 6 adds random items to rooms.
# Step 7 adds the monster to one room.
# Step 8 sets required items for winning.
inventory = []
current_room = start_room
required_items = []

# Learners test by editing these commands in code, not by typing in a shell.
scripted_moves = [
    'go south',
    'go north',
]

current_room, inventory = run_game(
    current_room,
    inventory,
    rooms,
    goal_room,
    required_items,
    monster_name,
    scripted_moves,
)
