from game import run_game

# Step 2: edit these word lists.
adjectives = [
    'ancient',
    'frozen',
    'golden',
    'silent',
    'wild',
]

nouns = [
    'forest',
    'amulet',
    'guardian',
    'lantern',
    'gate',
]

# Step 3 and 4 will replace these fixed names with random names.
start_room = 'Hall'
monster_room = 'Kitchen'
treasure_room = 'Dining Room'
goal_room = 'Garden'
item_one = 'key'
item_two = 'potion'
monster_name = 'monster'

# Step 5 builds the map layout.
rooms = {
    start_room: {
        'south': monster_room,
        'east': treasure_room,
    },
    monster_room: {
        'north': start_room,
    },
    treasure_room: {
        'west': start_room,
        'south': goal_room,
    },
    goal_room: {
        'north': treasure_room,
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
    'go east',
    f'get {item_two}',
    'go west',
    f'get {item_one}',
    'go east',
    'go south',
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
