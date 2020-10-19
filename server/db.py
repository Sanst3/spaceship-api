import sqlite3

import click
from flask import current_app

DB_PATH = "server/spaceship_db.db"
SCHEMA_PATH = "server/spaceship_schema.sql"

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def get_db():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = dict_factory

    return db

def init_db():
    db = get_db()

    with open(SCHEMA_PATH, 'r') as f:
        db.executescript(f.read())

# Inserts the insert query into the db and returns the id of the newly inserted object
# Returns None if insert fails
def insert_db(query, args=()):
    con = get_db()

    cur = con.cursor()
    try:
        cur.execute(query, args)
        con.commit()
    except sqlite3.IntegrityError as err:
        print(err)
        return None
    rowcount = cur.rowcount
    results = cur.lastrowid

    cur.close()
    con.close()

    return results if rowcount > 0 else None

# Used for delete queries and boolean of delete success
def delete_db(query, args=()):
    con = get_db()
    
    cur = con.cursor()
    
    cur.execute(query, args)
    con.commit()

    rowcount = cur.rowcount

    cur.close()
    con.close()

    return rowcount > 0

# Returns the row(s) obtained from the query
def select_db(query, args=(), one=False):
    con = get_db()

    cur = con.cursor().execute(query, args)
    con.commit()
    results = cur.fetchall()

    cur.close()
    con.close()

    return (results[0] if results else None) if one else results
