"""
Тип ошибки 2: Отсутствие возврата строки в __str__
Возникает, когда метод __str__ возвращает не строку, а объект другого типа, например, int.
Пример ошибки:
"""

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return self.age  # Ошибка: возвращается число, а не строка.
#
#
# s1 = Student('Иван', 16)
# print(s1)

"""
Решение:
Метод __str__ всегда должен возвращать строку.
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age} лет'


s1 = Student('Иван', 16)
print(s1)


