from . import db

def print_row(row):
    print("Starting print")
    for key in row.keys():
        print(str(key) + ": " + str(row[key]))

    print("Ending print")

def unpark_ship(ship_id):
    db.delete_db("DELETE FROM parking WHERE ship_id = ?", (ship_id,))

def park_ship(ship_id, location_id):
    db.insert_db("INSERT INTO parking (ship_id, location_id) VALUES (?, ?)", (ship_id, location_id))

def move_ship(ship_id, location_id):
    location = get_location_by_id(location_id)
    ret = False
    if (has_space(location)):
        ret = True
        unpark_ship(ship_id)
        park_ship(ship_id, location_id)

    return ret

def insert_location(city, planet, capacity):
    new_id = db.insert_db(
        "INSERT INTO location (city_name, planet_name, max_capacity) VALUES (?, ?, ?)",
        (city, planet, capacity)
    )

    return new_id

def insert_ship(name, model, status, location_id):
    location = get_location_by_id(location_id)
    if (has_space(location)):
        new_id = db.insert_db(
            "INSERT INTO ship (name, model, status) VALUES (?, ?, ?)",
            (name, model, status)
        )
        db.insert_db(
            "INSERT INTO parking (ship_id, location_id) VALUES (?, ?)",
            (new_id, location_id)
        )

    return new_id
    
def get_ship_by_name(name, model):
    ship = db.select_db(
        "SELECT * FROM ship WHERE name=? AND model=?",
        (name, model),
        True
    )

    return ship if ship else None

def get_ship_by_id(ship_id):
    ship = db.select_db(
        "SELECT * FROM ship WHERE id=?",
        (ship_id,),
        True
    )

    return ship if ship else None


def get_location_by_name(city, planet):
    location = db.select_db(
        "SELECT * FROM location WHERE city_name=? AND planet_name=?",
        (city, planet),
        True
    )

    return location if location else None

def get_location_by_id(location_id):
    location = db.select_db(
        "SELECT * FROM location WHERE id=?",
        (location_id,),
        True
    )

    return location if location else None


def has_space(location):
    return (location["max_capacity"] - fill_count(location)) > 0

def fill_count(location):
    
    query = "SELECT COUNT(*) AS count FROM locationw WHERE location.id=?"
    count = db.select_db(query, (location["id"],), True)

    return count["count"]