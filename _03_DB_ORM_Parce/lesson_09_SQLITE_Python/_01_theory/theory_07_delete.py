import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'databases\students.db')  # 1. Открываем соединение
    cursor = conn.cursor()

    # удаление данных по условию
    cursor.execute('DELETE FROM students where age > ?', (21,))
    conn.commit()

    # просто проверка
    cursor.execute('SELECT * FROM students;')
    students = cursor.fetchall()
    print(students)
    conn.close()
