import sqlite3

def create_db():
    conn = sqlite3.connect('database/user_database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users_info (
        id INTEGER PRIMARY KEY NOT NULL UNIQUE,
        user_id INTEGER NOT NULL UNIQUE,
        user_fullname TEXT NOT NULL,
        user_shortname TEXT,
        user_status TEXT,
        user_date_sub TEXT NOT NULL)
        ''')
    conn.commit()