DROP TABLE IF EXISTS ship;
DROP TABLE IF EXISTS location;
PRAGMA foreign_keys = ON;

CREATE TABLE ship (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, 
    model TEXT NOT NULL,
    status TEXT NOT NULL,
    parking_id INTEGER NOT NULL REFERENCES location (id)
);

CREATE TABLE location (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_name TEXT NOT NULL,
    planet_name TEXT NOT NULL,
    max_capacity INTEGER NOT NULL
);

CREATE TRIGGER delete_parkingless_ships
    AFTER 
    DELETE ON
    location
    BEGIN
        DELETE FROM ship WHERE parking_id = OLD.id;
    END;