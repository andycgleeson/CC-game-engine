from gameobjects import Location, Person, Article, Portal, Container
from db import *

def show_person_info(person_id):
    person = get_person_by_id(person_id)
    print(person.person_id)
    print(f"This persons name is '{person.name}'")
    containers = get_containers_by_owner(person.person_id)
    if len(containers) == 0:
        print("They are not carrying anything")
    else:
        for container in containers:
            print(f"They have a '{container.description}'")
            articles = get_articles_by_owner(container.container_id)
            for article in articles:
                print(f"The {container.description} contains {article.description}")
    print("\n")

def show_portal_info(portal_id):
    portal = get_portal_by_id(portal_id)
    print(portal.portal_id)
    print(portal.description)
    source = get_location_by_id(portal.source)
    destination = get_location_by_id(portal.destination)
    print(f"This portal goes from {source.name} to {destination.name}")
    if portal.status == "locked":
        key = get_article_by_id(portal.key)
        print(f"This portal is locked use key {key.name} to open it")
    elif portal.status == "open":
        print("This portal is open")
    else:
        print(f"Unknown portal status '{portal.status}'")
    print("\n")


def show_location_info(location_id):
    location = get_location_by_id(location_id)
    print(location.location_id)
    print(location.name)
    portals = get_portals_for_location(location_id);
    if len(portals) == 0:
        print("This location has no exit portals")
    else:
        for portal in portals:
            dest = get_location_by_id(portal.destination)
            print(f"A portal to the {portal.direction} goes to {dest.name}")
    containers = get_containers_by_owner(location_id)
    if len(containers) == 0:
        print("This location has no containers")
    else:
        for container in containers:
            print(f"This location has a container called {container.description}")
            items = get_container_contents(container.container_id)
            if len(items) == 0:
                print("\tThe container is empty")
            else:
                for item in items:
                    if isinstance(item, Article):
                        print(f"\tThe container contains the article {item.name}")
                    elif isinstance(item, Container):
                        print(f"\tThe container contains another container called {item.description}")

    articles = get_articles_by_owner(location_id)
    if len(articles) == 0:
        print("This location has no loose articles")
    else:
        for article in articles:
            print(f"article '{article.name}' is in this location")
    print("\n")

def show_article_info(article_id):
    print(article_id)
    article = get_article_by_id(article_id)
    print(f"{article.name}, {article.description}")
    owner = get_article_owner(article.owner_id)
    if isinstance(owner, Location):
        print(f"It is at a Location called '{owner.name}'")
    if isinstance(owner, Container):
        print(f"It is in a container called '{owner.description}'")
    if isinstance(owner, Person):
        print(f"It is held by a person called '{owner.name}'")

    print ("\n")

def show_container_info(container_id):
    print(container_id)
    container = get_container_by_id(container_id)
    print(f"This container is a {container.description}")
    if container.carryable:
        print("This container is carryable")
    else:
        print("This container cannot be moved")
    if container.status == "open":
        print("Container is not locked")
    elif container.status == "locked":
        key = get_article_by_id(container.key)
        print(f"Container is locked use '{key.name}' to open")
    else:
        print(f"Unknown container status '{container.status}'")
    items = get_container_contents(container_id)
    if len(items) == 0:
        print("This container has no contents")
    else:
        for item in items:
            if isinstance(item, Article):
                print(f"This container contains an article '{item .name}'")
            elif isinstance(item, Container):
                print(f"This container contains a container called '{item.description}'")
    print("\n")


print("Persons\n")

persons = get_persons()
for person in persons:
    show_person_info(person.person_id)


print("Portals\n")

portals = get_portals()
for portal in portals:
    show_portal_info(portal.portal_id)

print("Locations\n")

locations = get_locations()
for location in locations:
    show_location_info(location.location_id)

print ("Articles\n")

articles = get_articles()
for article in articles:
    show_article_info(article.article_id)

print("Containers\n")

containers = get_containers()
for container in containers:
    show_container_info(container.container_id)



