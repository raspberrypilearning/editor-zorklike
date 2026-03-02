#!/bin/python3
import random

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


def show_instructions(goal_room, required_items):
    print('''
Word Quest
========
Commands:
go [direction]
get [item]
''')
    print('Reach the ' + goal_room + ' with:')
    for item in required_items:
        print('- ' + item)


def show_status(current_room, inventory, rooms):
    print('---------------------------')
    print('You are in the ' + current_room)
    print('Inventory : ' + str(inventory))
    if 'item' in rooms[current_room]:
        print('You see a ' + rooms[current_room]['item'])
    print('---------------------------')


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
scripted_moves = [
    'go east',
    f'get {item_two}',
    'go west',
    f'get {item_one}',
    'go east',
    'go south',
]

show_instructions(goal_room, required_items)

for move in scripted_moves:
    show_status(current_room, inventory, rooms)
    move = move.strip().lower()
    print('> ' + move)

    parts = move.split()
    if len(parts) < 2:
        print('Use a two-word command, like: go north')
        continue

    command = parts[0]
    target = ' '.join(parts[1:])

    if command == 'go':
        if target in rooms[current_room]:
            current_room = rooms[current_room][target]
        else:
            print('You cannot go that way!')

    elif command == 'get':
        if 'item' in rooms[current_room] and rooms[current_room]['item'] == target:
            inventory.append(target)
            print('You picked up the ' + target)
            del rooms[current_room]['item']
        else:
            print('There is no ' + target + ' here!')
    else:
        print('Unknown command: ' + command)

    if 'item' in rooms[current_room] and rooms[current_room]['item'] == monster_name:
        print('The ' + monster_name + ' catches you... GAME OVER!')
        break

    if current_room == goal_room and all(item in inventory for item in required_items):
        print('You completed the quest... YOU WIN!')
        break
else:
    print('Scripted test finished.')
