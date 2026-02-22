import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'databases\example.db')   # 1. Открываем соединение
    cursor = conn.cursor()  # 2. Создаём курсор
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
        );
    """)  # 3. Выполняем запрос
    conn.commit()  # 4. Фиксируем изменения
    conn.close()
