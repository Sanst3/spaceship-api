DROP TABLE IF EXISTS ship;
DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS parking;

CREATE TABLE ship (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL, 
    model TEXT NOT NULL,
    status TEXT NOT NULL,
    UNIQUE(name, model)
);

CREATE TABLE location (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city_name TEXT NOT NULL,
    planet_name TEXT NOT NULL,
    max_capacity INTEGER NOT NULL,
    UNIQUE(city_name, planet_name)
);

CREATE TABLE parking (
    ship_id INTEGER NOT NULL,
    location_id INTEGER NOT NULL,

    FOREIGN KEY (ship_id)
        REFERENCES ship (id),
    FOREIGN KEY (location_id)
        REFERENCES location (id)
);