import sqlite3

conn = sqlite3.connect(r'databases/my_database.db')
cursor = conn.cursor()

# # Таблица пользователей
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     user_id INTEGER PRIMARY KEY,
#     name TEXT,
#     age INTEGER
#     )
# """)
#
# # Таблица заказов, где каждый заказ связан с пользователем (user_id)
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS orders (
#     order_id INTEGER PRIMARY KEY,
#     user_id INTEGER,
#     item TEXT,
#     FOREIGN KEY (user_id) REFERENCES users(user_id)
#     )
# """)
#
# conn.commit()
#
#
# # Добавляем пользователей
# cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 25))
# cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 30))
#
#
# # Добавляем заказы, указывая user_id
# cursor.execute('INSERT INTO orders (user_id, item) VALUES (?, ?)', (1, 'Ноутбук'))
# cursor.execute('INSERT INTO orders (user_id, item) VALUES (?, ?)', (1, 'Телефон'))
# cursor.execute('INSERT INTO orders (user_id, item) VALUES (?, ?)', (2, 'Часы'))
# conn.commit()

# Получаем все заказы Алисы (user_id = 1)
cursor.execute("""
SELECT users.name, orders.item
FROM users
JOIN orders ON users.user_id = orders.user_id
WHERE users.user_id = ?
""", (1,))

data = cursor.fetchall()
print(data)
