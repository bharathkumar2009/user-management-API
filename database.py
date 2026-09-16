import sqlite3

def get_connection():
    return sqlite3.connect("dtabase.db")
def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(""" CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    age INTEGER NOT NULL)""")

    connection.commit()
    connection.close()