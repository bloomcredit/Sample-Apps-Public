import sqlite3


def _get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_consumer_byid(consumer_id):
    conn = _get_db_connection()
    consumer = conn.execute('SELECT * FROM consumers WHERE consumer_id = ?',
                            (consumer_id,)).fetchone()
    conn.close()

    # Convert sqlite3.Row to dictionary if a valid row is fetched
    if consumer:
        return dict(consumer)
    return None


def insert_consumer(name, consumer_id):
    conn = _get_db_connection()
    conn.execute('INSERT INTO consumers (name, consumer_id) VALUES (?, ?)',
                 (name, consumer_id))
    conn.commit()
    conn.close()


def get_all_consumers():
    conn = _get_db_connection()
    consumers = conn.execute('SELECT * FROM consumers').fetchall()
    conn.close()

    # Convert each sqlite3.Row in consumers to a dictionary
    return [dict(consumer) for consumer in consumers]
