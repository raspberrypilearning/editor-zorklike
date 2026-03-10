import random

from game import run_game

adjectives = [
    'chocolate',
    'golden',
    'fizzy',
    'sweet',
    'candy',
    'wonka',
    'sugary',
    'mystery',
]

room_nouns = [
    'factory',
    'river',
    'elevator',
    'tunnel',
    'inventing room',
    'nut room',
    'tv room',
    'workshop',
]

object_nouns = [
    'ticket',
    'gobstopper',
    'bar',
    'blueberry',
    'oompa loompa',
    'toffee',
    'fudge',
    'caramel',
]


def random_phrase(noun_list):
    return random.choice(adjectives) + ' ' + random.choice(noun_list)


def unique_phrases(count, noun_list):
    phrases = set()
    while len(phrases) < count:
        phrases.add(random_phrase(noun_list))
    return list(phrases)


room_names = unique_phrases(4, room_nouns)
object_names = unique_phrases(3, object_nouns)
start_room = room_names[0].title()
monster_room = room_names[1].title()
treasure_room = room_names[2].title()
goal_room = room_names[3].title()
item_one = object_names[0]
item_two = object_names[1]
monster_name = object_names[2]

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

current_room, inventory = run_game(
    current_room,
    inventory,
    rooms,
    goal_room,
    required_items,
    monster_name,
)
