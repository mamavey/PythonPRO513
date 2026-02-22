import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'databases\students.db')  # 1. Открываем соединение
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT
    );
    """)

    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
                   ("Иван Иванов", 20, "Математика"))
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
                   ("Анна Смирнова", 21, "Физика"))
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
                   ("Дмитрий Петров", 23, "Химия"))
    conn.commit()  # 4. Фиксируем изменения
    conn.close()
