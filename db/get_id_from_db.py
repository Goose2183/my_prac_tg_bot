import sqlite3

async def get_users_id():
    with sqlite3.connect('database/user_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users_info")
        user_ids = cursor.fetchall()
        return tuple(user_id[0] for user_id in user_ids)
