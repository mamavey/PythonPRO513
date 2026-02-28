"""
Тип ошибки 2: Ошибки в связях между таблицами

При создании связей между таблицами с помощью FOREIGN KEY важно указывать правильные имена полей.
Если внешний ключ (FOREIGN KEY) ссылается на несуществующее поле,
это приведет к ошибке при выполнении SQL-запроса.
"""

import sqlite3

conn = sqlite3.connect(r"databases/my_database.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")
# # Таблица пользователей
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users1 (
#     user_id INTEGER PRIMARY KEY,
#     name TEXT
# )
# """)
#
# # Таблица заказов, где каждый заказ связан с пользователем (user_id)
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS orders1 (
#     order_id INTEGER PRIMARY KEY,
#     user_id INTEGER,
#     item TEXT,
#     FOREIGN KEY (user_id) REFERENCES users1(uiid)
# )
# """)

conn.commit()

"""
Решение:

Необходимо убедиться, что внешний ключ ссылается на существующее поле:
"""

# Таблица пользователей
cursor.execute("""
CREATE TABLE IF NOT EXISTS users1 (
    user_id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    item TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)  -- Теперь ссылка корректная
)
""")

conn.commit()
