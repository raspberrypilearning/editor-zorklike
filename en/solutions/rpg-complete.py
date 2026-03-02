#!/bin/python3
import random

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

show_instructions(goal_room, required_items)

while True:
    show_status(current_room, inventory, rooms)

    move = ''
    while move == '':
        move = input('>').strip().lower()

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
