import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

DB_PATH = "backend/spaceship_db.db"
SCHEMA_PATH = "backend/spaceship_schema.sql"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row

    return db


def close_db(e=None):
    db = getattr(g, '_database', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with open(SCHEMA_PATH, 'r') as f:
        db.executescript(f.read())

def query_db(query, args=()):
    con = get_db()
    cur = con.cursor().execute(query, args)
    results = cur.fetchall()
    cur.close()

    return results if results else None

def insert_location(city, planet, capacity):
    query_db(
        "INSERT INTO location (city_name, planet_name, max_capacity) VALUES (?, ?, ?)",
        (city, planet, capacity)
    )