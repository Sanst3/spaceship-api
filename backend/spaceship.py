from . import db

def print_row(row):
    print("Starting print")
    for key in row.keys():
        print(str(key) + ": " + str(row[key]))

    print("Ending print")

def print_row_list(list):
    for row in list:
        print_row(row)

def print_parked_ships(location_id):
    for ship in get_parked_ships(location_id):
        print_row(ship)


def move_ship(ship_id, location_id):
    location = get_location_by_id(location_id)
    ret = False
    if (has_space(location)):
        ret = True
        db.insert_db("UPDATE ship SET parking_id = ? WHERE id = ?", (location_id, ship_id))

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
            "INSERT INTO ship (name, model, status, parking_id) VALUES (?, ?, ?, ?)",
            (name, model, status, location_id)
        )

    return new_id


def delete_location(location_id):
    db.delete_db("DELETE FROM location WHERE id = ?", (location_id,))

def delete_ship(ship_id):
    db.delete_db("DELETE FORM ship WHERE id = ?", (ship_id,))

def get_ship_by_id(ship_id):
    ship = db.select_db(
        "SELECT * FROM ship WHERE id=?",
        (ship_id,),
        True
    )

    return ship if ship else None

def get_location_by_id(location_id):
    location = db.select_db(
        "SELECT * FROM location WHERE id=?",
        (location_id,),
        True
    )

    return location if location else None

def get_parked_ships(location_id):
    return db.select_db("SELECT * FROM ship WHERE parking_id = ?", (location_id,))

def get_locations():
    return db.select_db("SELECT * FROM location")

def has_space(location):
    return (location["max_capacity"] - fill_count(location)) > 0

def fill_count(location):
    
    query = "SELECT COUNT(*) AS count FROM ship WHERE parking_id=?"
    count = db.select_db(query, (location["id"],), True)

    return count["count"]