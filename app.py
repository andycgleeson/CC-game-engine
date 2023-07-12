from gameobjects import Location, Person, Article, Portal, Container
from help import *
from db import *
from utils import join_str_list

print("CC type game experiment")
print("\n\n")


def get_person_info(person_id):
    person = get_person_by_id(person_id)
    print(f"This persons name is '{person.name}'")
    containers = get_containers_by_owner(person.person_id)
    for container in containers:
        print(f"They have a '{container.description}'")
        articles = get_articles_by_owner(container.container_id)
        for article in articles:
            print(f"The {container.description} contains {article.description}")


def current_room_info(person_id):
    person = get_person_by_id(person_id)
    current_room = get_location_by_id(person.location)
    exits = get_portals_for_location(current_room.location_id)
    exit_str = [exit.direction for exit in exits]
    print(f"You are in the {current_room.name} it has exits to the {join_str_list(exit_str)}")


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
    print(f'{params}')


def PICKUP(params):
    print(f'{params}')


def DROP(params):
    print(f'{params}')


def LOOKAT(params):
    print(f'{params}')
    for param in params[1:]:
        if param == 'ROOM':
            print(param)
        elif param == 'ME':
            print(param)


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
