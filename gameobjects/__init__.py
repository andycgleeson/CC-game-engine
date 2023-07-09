from dataclasses import dataclass

@dataclass
class Location(object):
    location_id: str = None
    name: str = None
    description: str = None
    dark: int = 0

@dataclass
class Portal(object):
    portal_id: str = None
    source: str = None
    destination: str = None
    description: str = None
    direction: str = None
    status: str = None
    key: str = None
    open_description: str = None
    closed_description: str = None
    transit_description: str = None

@dataclass
class Person(object):
    person_id: str = None
    name: str = None
    location: str = None

@dataclass
class Article(object):
    article_id: str = None
    owner_id: str = None
    name: str = None
    description: str = None
    properties: str = None

@dataclass
class Container(object):
    container_id: str = None
    owner_id: str = None
    description: str = None
    capacity: int = 0
    carryable: bool = False
    status: str = None
    key: str = None
        

    
    
        


