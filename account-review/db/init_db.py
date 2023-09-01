import sqlite3

def create():
    connection = sqlite3.connect('database.db')

    with open('./db/schema.sql') as f:
        connection.executescript(f.read())

    connection.commit()
    connection.close()