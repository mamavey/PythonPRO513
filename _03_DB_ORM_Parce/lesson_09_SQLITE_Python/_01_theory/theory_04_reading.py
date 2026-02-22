import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'databases\students.db')  # 1. Открываем соединение
    cursor = conn.cursor()

    # fetchall() — получает все строки из результата запроса.
    cursor.execute('SELECT * FROM students;')
    students = cursor.fetchall()
    # print(students)
    for s_id, name, age, course in students:
        print(f'id - {s_id}, name - {name}, age - {age}, course - {course}')
    print()

    # Метод fetchone() возвращает первую строку результата запроса в виде кортежа.
    cursor.execute('SELECT * FROM students;')
    student = cursor.fetchone()
    print(student)
    student = cursor.fetchone()
    print(student)
    student = cursor.fetchone()
    print(student)
    student = cursor.fetchone()
    print(student)

    # cursor.execute('SELECT * FROM students;')
    # param = True
    # while param:
    #     input('Нажмите ENTER для получения записи: ')
    #     data = cursor.fetchone()
    #     if not data:
    #         print(f'Все данные извлечены')
    #         param = False
    #     else:
    #         print(data)

    # fetchmany(n) — получает n строк из результата запроса.
    cursor.execute('SELECT * FROM students;')
    while True:
        rows = cursor.fetchmany(2)
        if not rows:
            break
        print(rows)

    for row in rows:
        print(row)

    conn.close()
