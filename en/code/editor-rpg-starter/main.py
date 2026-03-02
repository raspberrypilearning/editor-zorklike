from game import run_game, unique_phrases
from word_lists import adjectives, nouns


# Build one random adventure each time the player clicks Run.
names = unique_phrases(7, adjectives, nouns)
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

current_room, inventory = run_game(
    current_room,
    inventory,
    rooms,
    goal_room,
    required_items,
    monster_name,
)
