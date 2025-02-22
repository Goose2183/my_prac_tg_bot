import sqlite3
async def get_statistic():
    with sqlite3.connect('database/user_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                COUNT(*) AS total_users,
                SUM(CASE WHEN user_status = 'banned' THEN 1 ELSE 0 END) AS banned_users,
                SUM(CASE WHEN user_status = 'subscribed' THEN 1 ELSE 0 END) AS subscribed_users
            FROM users_info
            """)

        result = cursor.fetchone()
        return result