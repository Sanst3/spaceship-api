import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

DB_PATH = "backend/spaceship_db.db"
SCHEMA_PATH = "backend/spaceship_schema.sql"

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB_PATH)
    db.row_factory = dict_factory

    return db


def close_db(e=None):
    db = getattr(g, '_database', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with open(SCHEMA_PATH, 'r') as f:
        db.executescript(f.read())

# Inserts the insert query into the db and returns the id of the newly inserted object
# Returns None if insert fails
def insert_db(query, args=()):
    con = get_db()
    
    cur = con.cursor()
    old_rowcount = cur.rowcount
    cur.execute(query, args)
    new_rowcount = cur.rowcount
    results = cur.lastrowid
    cur.close()

    return results if new_rowcount != old_rowcount else None

def delete_db(query, args=()):
    con = get_db()
    
    cur = con.cursor()
    cur.execute(query, args)
    cur.close()

# Returns the row(s) obtained from the query
def select_db(query, args=(), one=False):
    con = get_db()
    cur = con.cursor().execute(query, args)
    results = cur.fetchall()
    cur.close()

    return (results[0] if results else None) if one else results
