"""
Задача 1: Управление классами в школе

Ситуация: представьте, что вы — классный руководитель и хотите автоматизировать процесс учёта учеников.
Нам нужно создать программу, которая позволит добавлять учеников в класс,
ставить им оценки и видеть список всех учеников с их средними баллами.

Задача: создайте программу, которая позволяет:

Добавлять учеников в список класса.
Присваивать оценки ученикам.
Просматривать всех учеников с их средними баллами.
"""
from classes.ClassStudent import Student
from classes.ClassClassroom import Classroom


def main():
    classroom = Classroom()
    while True:
        command = input('Введите команду (1 - add student, 2 - add grade, 3 - show students, 0 - exit): ').strip()
        if command == '1':
            name = input('Введите имя студента: ').strip().title()
            student = Student(name)
            classroom.add_student(student)
            print(f'Студент {name} добавлен')
        elif command == '2':
            name = input('Введите имя студента: ').strip().title()
            while True:
                grade = float(input('Введите оценку или 0 для прекращения ввода: '))
                if grade == 0:
                    break
                else:
                    print(classroom.add_grade_to_student(name, grade))
        elif command == '3':
            classroom.show_students()
        elif command == '0':
            print('Программа завершена')
            break
        else:
            print('Неизвестная команда. Попробуйте снова')


if __name__ == '__main__':
    main()
