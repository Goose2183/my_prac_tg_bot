import sqlite3
import logging

async def add_user(user_id: int, user_fullname: str, user_shortname: str, user_status: str, user_date_sub: str):
    try:
        with sqlite3.connect('database/user_database.db') as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users_info '
                           '(user_id, '
                           'user_fullname, '
                           'user_shortname, '
                           'user_status, '
                           'user_date_sub) '
                           'VALUES (?, ?, ?, ?, ?)',
                           (user_id,
                            user_fullname,
                            user_shortname,
                            user_status,
                            user_date_sub))

    except sqlite3.IntegrityError:
        logging.info(f"Пользователь: @{user_shortname} уже добавлен в БД")
