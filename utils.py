# Utility functions for CC type game engine
from db import *

def join_str_list(str_list):
    # return string list as a string in the format 'a' or 'a' and 'b' or 'a, b and c'
    if len(str_list) == 0:
        return ""
    elif len(str_list) == 1:
        return str_list[0]
    else:
        return f"{', '.join(str_list[:-1])} and {str_list[-1]}"



def get_person_info(person_id):
    person = get_person_by_id(person_id)
    print(f"Hi {person.name}")
    containers = get_containers_by_owner(person.person_id)
    for container in containers:
        articles = get_articles_by_owner(container.container_id)
        if len(articles) > 0:
            contents = f"which contains a {join_str_list([article.name for article in articles])}"
        else:
            contents = "which is empty"
        print(f"You have a '{container.description}' {contents}.")
    articles = get_articles_by_owner(person.person_id)
    if len(articles) > 0:
        print(f"you are holding {join_str_list([article.name for article in articles])}.")
    print("\n")


def get_room_info(location_id):
    current_room = get_location_by_id(location_id)
    exits = get_portals_for_location(current_room.location_id)
    if len(exits) > 0:
        exit_str = f"As far as i can see it has exits to the {join_str_list([exit.direction for exit in exits])}"
    else:
        exit_str = 'it has no obvious exits'
    print(f"You are in the {current_room.name}\n{current_room.description}.\n{exit_str}")
    containers = get_containers_by_owner(location_id)
    if len(containers) > 0:
        print(f"This location has {join_str_list([container.description for container in containers])}")
    articles = get_articles_by_owner(location_id)
    if len(articles) > 0:
        print(f"This location has {join_str_list([article.name for article in articles])}")
    print("\n")


