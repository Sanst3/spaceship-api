from . import db

# Debug printers
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

# Changes the location of a ship given its ship id and the new location's id
# Returns True if the move was successful and False if not
def move_ship(ship_id, location_id):
    location = get_location_by_id(location_id)
    ret = False
    if (has_space(location) and is_operational(ship_id)):
        ret = True
        db.insert_db("UPDATE ship SET parking_id = ? WHERE id = ?", (location_id, ship_id))

    return ret

# Inserts a new location to the database
# Returns the id of the newly created location
def insert_location(city, planet, capacity):
    new_id = db.insert_db(
        "INSERT INTO location (city_name, planet_name, max_capacity) VALUES (?, ?, ?)",
        (city, planet, capacity)
    )

    return new_id


# Inserts a new ship to the database
# Returns the id of the newly created ship
def insert_ship(name, model, status, location_id):
    location = get_location_by_id(location_id)
    decoded_status = decode_status(status)

    if (has_space(location) and decoded_status):
        new_id = db.insert_db(
            "INSERT INTO ship (name, model, status, parking_id) VALUES (?, ?, ?, ?)",
            (name, model, decoded_status, location_id)
        )
    else:
        new_id = None

    return new_id

# Changes a ship's status given an ship_id and a status code
# 0: Decommissioned
# 1: Maintenance
# 2: Operational
# Returns True if update was successful, False if otherwise
def change_ship_status(ship_id, status):
    decoded_status = decode_status(status)
    ret = False
    if decoded_status:
        
        result = db.insert_db("UPDATE ship SET status = ? WHERE id = ?", (decoded_status, ship_id))
        if result != None:
            ret = True
    
    return ret


# Deletes a location from the database given its location id
# Returns True if delete successful, False if otherwise
def delete_location(location_id):
    return db.delete_db("DELETE FROM location WHERE id = ?", (location_id,))

# Deletes a ship from the database given its ship id
# Returns True if delete successful, False if otherwise
def delete_ship(ship_id):
    return db.delete_db("DELETE FROM ship WHERE id = ?", (ship_id,))

# Gets a ship from the database given its ship id
# Returns the query result if found, and None if no result was found
def get_ship_by_id(ship_id):
    ship = db.select_db(
        "SELECT * FROM ship WHERE id=?",
        (ship_id,),
        True
    )

    return ship

# Gets a location from the database given its location id
# Returns the query result if found, and None if no result was found
def get_location_by_id(location_id):
    location = db.select_db(
        "SELECT * FROM location WHERE id=?",
        (location_id,),
        True
    )

    return location

# Gets all the ships parked in a location given a location's id
# Returns a list of ships if found, and None if no result was found
def get_parked_ships(location_id):
    return db.select_db("SELECT * FROM ship WHERE parking_id = ?", (location_id,))

# Retrieves a list of all locations in the database
# Returns a list of locations, and None if no locations exist
def get_locations():
    return db.select_db("SELECT * FROM location")

# Checks if a location still has any empty spaces
# Returns True if location's max capacity hasn't been reached, False otherwise
def has_space(location):
    if not location:
        return False

    return (location["max_capacity"] - fill_count(location)) > 0

# Returns the amount of ships parked in a location
def fill_count(location):
    query = "SELECT COUNT(*) AS count FROM ship WHERE parking_id=?"
    count = db.select_db(query, (location["id"],), True)

    return count["count"]

# Decodes the status codes into the strings they represent
def decode_status(status):
    if status == '0':
        return "Decommissioned"
    elif status == '1':
        return "Maintenance"
    elif status == '2':
        return "Operational"
    else:
        return None

# Checks if a ship's status is operational
# Returns True if ship is operational, False otherwise
def is_operational(ship_id):
    result = False
    ship = db.select_db("SELECT * FROM ship WHERE id = ?", (ship_id,), True)
    if ship:
        result = ship["status"] == "Operational"

    return result