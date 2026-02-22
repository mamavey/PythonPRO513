"""
Задача 2: Работа с таблицей пользователей: обновление и удаление данных

Ситуация:
Вы продолжаете работать с базой данных пользователей.
В этой задаче вам нужно будет обновить информацию о некоторых пользователях и удалить старые данные.

Задача:
Обновите возраст некоторых пользователей.
Удалите пользователей с определённым возрастом из базы данных.
"""

import sqlite3


def display_data(cursor_obj, table_name):
    try:
        cursor_obj.execute(f"SELECT * FROM {table_name};")
    except sqlite3.Error as err:
        print(f'{type(err).__name__} >> {err}')
    else:
        data = cursor_obj.fetchall()
        for row in data:
            print(row)
    print()


if __name__ == '__main__':
    conn = sqlite3.connect(r'databases/users.db')
    cursor = conn.cursor()
    # try:
    #     cursor.execute("""
    #         UPDATE users
    #         SET age = age + 2
    #         WHERE user_id = 1;
    #         """)
    #     cursor.execute("""
    #         UPDATE users
    #         SET age = age + 3
    #         WHERE email = 'alexey@example.com';
    #         """)
    # except sqlite3.Error as err:
    #     print(f'{type(err).__name__} >> {err}')
    # else:
    #     conn.commit()

    display_data(cursor, 'users')
    print()

    try:
        cursor.execute("""
        DELETE FROM users
        WHERE AGE < 25;
        """)
    except sqlite3.Error as err:
        print(f'{type(err).__name__} >> {err}')
    else:
        conn.commit()
    display_data(cursor, 'users')
    print()

    if conn:
        conn.close()
