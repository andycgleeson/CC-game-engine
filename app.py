from gameobjects import Location, Person, Article, Portal, Container
from help import *
from db import *
from utils import join_str_list, get_person_info, get_room_info

print("CC type game experiment")
print("\n\n")


def current_room_info(person_id):
    person = get_person_by_id(person_id)
    current_room = get_location_by_id(person.location)
    exits = get_portals_for_location(current_room.location_id)
    if len(exits) > 0:
        exit_str = f"There are exits to the {join_str_list([exit.direction for exit in exits])}."
    else:
        exit_str = 'There are no obvious exits'
    print(f"You are in the {current_room.name}. {exit_str}")


commands = ('QUIT', 'GO', 'PICKUP', 'DROP', 'LOOKAT', 'USE', 'HELP')
# Every command must start with a different letter to allow short form entry

directions = ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'UP', 'DOWN')

direction_names = {'N': 'North',
                   'NE': 'North East',
                   'E': 'West',
                   'SE': 'South East',
                   'S': 'South',
                   'SW': 'South West',
                   'W': 'West',
                   'NW': 'North West'}


def process_command(input_str):
    input_str = input_str.upper()
    params = input_str.split(" ")
    found = False
    for cmd in commands:
        if params[0] == cmd or params[0] == cmd[0]:
            eval(cmd + '(params)')
            found = True
    if not found:
        print(f"{params[0]} is not a valid command. use 'HELP' for more info")


def QUIT(params):
    # Quit the game
    if input('Do you really want to quit Y/N? ').upper() == 'Y':
        quit()


def GO(params):
    # Move to another location
    person = get_person_by_id(get_default_user_id())
    portals = get_portals_for_location(person.location)
    selected_portal = None
    for portal in portals:
        if params[1] == portal.direction:
            selected_portal = portal
            break
    if not selected_portal:
        print('I cannot find an exit in that direction')
    else:
        if selected_portal.status == 'locked':
            print(selected_portal.closed_description)
        else:
            set_person_location(person.person_id, portal.destination)
            print(selected_portal.transit_description)
    print('\n')


def PICKUP(params):
    print(f'{params}')


def DROP(params):
    print(f'{params}')


def LOOKAT(params):
    person = get_person_by_id(get_default_user_id())
    current_room = get_location_by_id(person.location)
    for param in params[1:]:
        if param == 'ROOM':
            get_room_info(current_room.location_id)
            break
        elif param == 'ME':
            get_person_info(person.person_id)
            break
        else:
            pass
            # anything else that could be looked at
            # portals
            # containers
            # articles
            # persons
        print(f"I couldn't find anything called {param} to look at\n")


def USE(params):
    print(f'{params}')


def HELP(params):
    if len(params) < 2:
        print(help_gen)
    else:
        found = False
        for cmd in commands:
            if params[1] == cmd or params[1] == cmd[0]:
                eval(f'print(help_{cmd.lower()})')
                found = True
                break
        if not found:
            print(f"I cannot find any help for '{params[1]}'")


while 1:
    current_room_info(get_default_user_id())
    process_command(input("What would you like to do? : "))
