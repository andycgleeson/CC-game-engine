from gameobjects import Location, Person, Article, Portal, Container
from db import (get_persons,
                get_portals,
                get_locations,
                get_articles,
                get_containers,
                get_person_by_id,
                get_location_by_id,
                get_containers_by_owner,
                get_articles_by_owner,
                get_portals_for_location
                )

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


def current_room_info():
    person = get_person_by_id(person_id)
    current_room = get_location_by_id(person.location)
    exits = get_portals_for_location(current_room)
    exit_str = ", ".join([exit.direction for exit in exits])
    print(f"The room you are in has {len(exits)} exits, they are {exit_str}")

get_person_info('7b1b7ad0-a411-48ae-8d4f-72704696fbad')
current_room_info('7b1b7ad0-a411-48ae-8d4f-72704696fbad')