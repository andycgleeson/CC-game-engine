from gameobjects import Location, Person, Article, Portal, Container
import sqlite3

def get_list(sql, params):
    with sqlite3.connect("./game.sqlite3") as connection:
        a = params
        cursor = connection.cursor()
        rows = cursor.execute(sql, params).fetchall()
        return rows

def get_row(sql, params):
    with sqlite3.connect("./game.sqlite3") as connection:
        a = params
        cursor = connection.cursor()
        row = cursor.execute(sql, params).fetchone()
        return row

def set_row(sql, params):
    with sqlite3.connect("./game.sqlite3") as connection:
        a = params
        cursor = connection.cursor()
        cursor.execute(sql, params)
        connection.commit()
        return cursor.lastrowid

def delete_item_by_id(table, id_name, item_id, params):
    with sqlite3.connect("./game.sqlite3") as connection:
        a = params
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {table} WHERE {id_name} = '{item_id}'")
        connection.commit()
        return cursor.lastrowid

# settings

def get_default_user_id():
    sql = f"SELECT value FROM settings WHERE parameter = 'default_user'"
    return get_row(sql, [])[0]

# Persons

def get_persons():
    sql = f"SELECT * FROM persons"
    rows = get_list(sql, [])
    return [Person(*row) for row in rows]

def get_person_by_id(person_id):
    sql = f"SELECT * FROM persons WHERE person_id = '{person_id}'"
    return Person(*get_row(sql, []))

def set_person_location(person_id, new_location):
    sql = f"UPDATE persons SET location = '{new_location}' WHERE person_id = '{person_id}'"
    return set_row(sql, [])

# Locations

def get_locations():
    sql = f"SELECT * FROM locations"
    rows = get_list(sql, [])
    return [Location(*row) for row in rows]

def get_location_by_id(location_id):
    sql = f"SELECT * FROM locations where location_id = '{location_id}'"
    row = get_row(sql, [])
    return Location(*row)

# Portals

def get_portals():
    sql = f"SELECT * FROM portals"
    rows = get_list(sql, [])
    return [Portal(*row) for row in rows]

def get_portal_by_id(portal_id):
    sql = f"SELECT * FROM portals where portal_id = '{portal_id}'"
    row = get_row(sql, [])
    return Portal(*row)

def get_portals_for_location(location_id):
    sql = f"SELECT * FROM portals WHERE source = '{location_id}'"
    rows = get_list(sql, [])
    return [Portal(*row) for row in rows]

# Articles

def get_articles():
    sql = f"SELECT * FROM articles"
    rows = get_list(sql, [])
    return [Article(*row) for row in rows]

def get_articles_by_owner(owner_id):
    sql = f"SELECT * FROM articles WHERE owner_id = '{owner_id}'"
    rows = get_list(sql, [])
    return [Article(*row) for row in rows]

def get_article_by_id(article_id):
    sql = f"SELECT * FROM articles where article_id = '{article_id}'"
    row = get_row(sql, [])
    return Article(*row)


def set_article_owner(article_id, owner_id):
    sql = f"UPDATE articles SET owner_id = '{owner_id}' WHERE article_id = '{article_id}'"
    return set_row(sql, [])

def get_article_owner(owner_id):
    sql = f"SELECT * FROM persons where person_id = '{owner_id}'"
    row = get_row(sql, [])
    if row != None:
        return Person(*row)
    sql = f"SELECT * FROM containers where container_id = '{owner_id}'"
    row = get_row(sql, [])
    if row != None:
        return Container(*row)
    sql = f"SELECT * FROM locations where location_id = '{owner_id}'"
    row = get_row(sql, [])
    if row != None:
        return Location(*row)



# Containers

def get_containers():
    sql = f"SELECT * FROM containers"
    rows = get_list(sql, [])
    return [Container(*row) for row in rows]


def get_containers_by_owner(owner_id):
    sql = f"SELECT * FROM containers WHERE owner_id = '{owner_id}'"
    rows = get_list(sql, [])
    return [Container(*row) for row in rows]

def set_container_owner(container_id, owner_id):
    sql = f"UPDATE container SET owner_id = '{owner_id}' WHERE container_id = '{container_id}'"
    return set_row(sql, [])

def get_container_by_id(container_id):
    sql = f"SELECT * FROM containers WHERE container_id = '{container_id}'"
    row = get_row(sql, [])
    return Container(*row)

def get_container_contents(container_id):
    contents = []
    sql = f"SELECT * FROM articles where owner_id = '{container_id}'"
    rows = get_list(sql, [])
    if len(rows) > 0:
        contents.extend([Article(*row) for row in rows])
    sql = f"SELECT * FROM containers where owner_id = '{container_id}'"
    rows = get_list(sql, [])
    if len(rows) > 0:
        contents.extend([Container(*row) for row in rows])
    return contents






