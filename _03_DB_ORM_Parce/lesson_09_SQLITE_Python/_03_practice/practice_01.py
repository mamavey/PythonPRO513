"""
Задача 1: Создание базы данных для управления пользователями с использованием SQLite3 в Python

Ситуация:
Вы разрабатываете приложение для управления пользователями.
Вам нужно создать базу данных SQLite, которая будет содержать таблицу с данными о пользователях.
Она должна включать информацию о пользователях, их возрасте и адресе email.

Задача:
Создайте таблицу users, которая будет хранить информацию о пользователях.
Затем выполните запросы для добавления данных,
чтения данных и фильтрации записей по возрасту с использованием SQLite3 в Python.
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
    #     CREATE TABLE IF NOT EXISTS users (
    #         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    #         name TEXT NOT NULL,
    #         age INTEGER NOT NULL,
    #         email TEXT UNIQUE NOT NULL
    #         );
    #         """)
    #
    #     cursor.executemany("""
    #     INSERT INTO users (name, age, email) VALUES (?, ?, ?)
    #     """, [
    #         ('Иван Иванов', 28, 'ivan@example.com'),
    #         ('Мария Смирнова', 34, 'maria@example.com'),
    #         ('Петр Петров', 22, 'peter@example.com'),
    #         ('Алексей Иванов', 25, 'alexey@example.com'),
    #         ('Ольга Сидорова', 29, 'olga@example.com')
    #     ])
    # except sqlite3.Error as err:
    #     print(f'Ошибка: {type(err).__name__} >> {err}')
    # else:
    #     conn.commit()

    # user_table = input('Из какой таблицы извлечь все данные: ')
    # display_data(cursor, user_table)

    user_table = input('Из какой таблицы данные: ')
    users_age = int(input('Введите минимальный возраст пользователя: '))
    try:
        cursor.execute(f"SELECT name, age, email FROM {user_table} WHERE age >= {users_age};")
    except sqlite3.Error as err:
        print(f'{type(err).__name__} >> {err}')
    else:
        filtered_data = cursor.fetchall()
        for filtered_row in filtered_data:
            print(filtered_row)
    print()

    if conn:
        conn.close()
