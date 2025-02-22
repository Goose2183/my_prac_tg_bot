import sqlite3

async def banned_user(user_id):
    with sqlite3.connect('database/user_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users_info SET user_status = 'banned' WHERE user_id = ?", (user_id,))
        conn.commit()

async def unbanned_user(user_id):
    with sqlite3.connect('database/user_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users_info SET user_status = 'subscribed' WHERE user_id = ?", (user_id,))
        conn.commit()