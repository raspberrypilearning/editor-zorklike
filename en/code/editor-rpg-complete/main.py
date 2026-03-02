import random

from game import run_game

adjectives = [
    'ancient',
    'brave',
    'crystal',
    'dusty',
    'ember',
    'frozen',
    'golden',
    'hidden',
]

nouns = [
    'archive',
    'amulet',
    'beast',
    'citadel',
    'compass',
    'forest',
    'gate',
    'guardian',
    'lantern',
    'path',
    'temple',
    'vault',
]


def random_phrase():
    return random.choice(adjectives) + ' ' + random.choice(nouns)


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

rooms = {
    start_room: {
        'south': monster_room,
        'east': treasure_room,
        'item': item_one,
    },
    monster_room: {
        'north': start_room,
        'item': monster_name,
    },
    treasure_room: {
        'west': start_room,
        'south': goal_room,
        'item': item_two,
    },
    goal_room: {
        'north': treasure_room,
    },
}

inventory = []
current_room = start_room
required_items = [item_one, item_two]

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
