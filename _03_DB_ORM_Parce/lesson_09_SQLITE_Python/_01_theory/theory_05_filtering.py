import sqlite3

if __name__ == '__main__':
    conn = sqlite3.connect(r'databases\students.db')  # 1. Открываем соединение
    cursor = conn.cursor()

    subjects = ['Математика', 'Химия']
    courses_students = []
    for subj in subjects:
        cursor.execute('SELECT * FROM students WHERE course = ?', (subj,))
        course_students = cursor.fetchall()
        courses_students.append(course_students)

    conn.close()
    print(courses_students)
