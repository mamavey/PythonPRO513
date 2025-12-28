"""
Тип ошибки 6: Несоответствие между __repr__ и __init__
Появляется, когда метод __repr__ возвращает строку, которую невозможно использовать для создания аналогичного объекта.
"""
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return f"Student({self.name}, {self.age})"  # Ошибка: пропущены кавычки вокруг имени.
#
#
# if __name__ == '__main__':
#     student = Student('Peter', 16)
#     print(student)
#     print(repr(student))
#     print(student.__repr__())
#     # student = Student(Peter, 16)

"""
Решение:

__repr__ должен возвращать строку, которая позволяет создать аналогичный объект.
"""

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student('{self.name}', {self.age})"


if __name__ == '__main__':
    student = Student('Peter', 16)
    print(repr(student))
    student = Student('Peter', 16)
