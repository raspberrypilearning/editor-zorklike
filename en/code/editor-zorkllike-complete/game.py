# Runs the text adventure game loop.

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


def run_game(current_room, inventory, rooms, goal_room, required_items, monster_name, scripted_moves=None):
    show_instructions(goal_room, required_items)

    move_index = 0

    while True:
        show_status(current_room, inventory, rooms)

        if scripted_moves is not None:
            if move_index >= len(scripted_moves):
                print('Scripted test finished.')
                break
            move = scripted_moves[move_index].strip().lower()
            move_index += 1
            print('> ' + move)
        else:
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

    return current_room, inventory
