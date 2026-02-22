"""
Тип ошибки 1: Метод commit() не использован после внесения изменений в базу данных
Часто ошибки возникают, когда мы забываем вызвать метод commit() после внесения изменений в базу данных.
Например, если не вызвать commit()
после таких операций, как INSERT, UPDATE или DELETE, то изменения не будут занесены в базу.
"""

import sqlite3

# conn = sqlite3.connect(r"databases\example.db")
# cursor = conn.cursor()
#
# cursor.execute("INSERT INTO users (name, age) VALUES ('Иван', 32)")
# # Нет вызова commit()
# # просто проверка
# cursor.execute("SELECT * FROM users;")
# users = cursor.fetchall()
# conn.close()
# print(users)
#
# conn = sqlite3.connect(r"databases\example.db")
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM users;")
# users = cursor.fetchall()
# print(users)
# conn.close()

"""
После любых изменений в базе необходимо вызвать commit() или настроить параметр conn.autocommit = True
"""
conn = sqlite3.connect(r"databases\example.db")
conn.autocommit = True
cursor = conn.cursor()
cursor.execute("INSERT INTO users (name, age) VALUES ('Петр', 33)")

cursor.execute("SELECT * FROM users;")
users = cursor.fetchall()
print(users)
conn.close()
