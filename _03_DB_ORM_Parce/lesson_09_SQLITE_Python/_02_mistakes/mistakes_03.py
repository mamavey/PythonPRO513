"""
Тип ошибки 3: Использование неподключённого соединения
Иногда ошибки возникают, когда мы пытаемся выполнить запрос после того, как соединение с базой данных было закрыто.
Пример ошибки:
"""

import sqlite3

conn = sqlite3.connect(r"databases/example.db")
cursor = conn.cursor()

conn.close()  # Закрываем соединение
#
# cursor.execute("SELECT * FROM users")

"""
Решение:

Используйте try except для безопасной работы.
"""

try:
    cursor.execute("SELECT * FROM users")
except Exception as e:
    print(f"Соединение с базой данных закрыто. {e}")