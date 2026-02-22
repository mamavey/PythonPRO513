import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'databases\students.db')  # 1. Открываем соединение
    cursor = conn.cursor()

    # обновление данных по условию
    cursor.execute('UPDATE students SET course = ? where name = ?', ('Информатика', 'Иван Иванов'))
    conn.commit()

    # просто проверка
    cursor.execute('SELECT * FROM students;')
    students = cursor.fetchall()
    print(students)
    conn.close()
