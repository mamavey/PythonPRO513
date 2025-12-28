# """
# Тип ошибки 1: Неправильная реализация метода __add__
# Ошибка возникает, когда при сложении двух объектов не создаётся новый объект.
# Пример ошибки:
# """
#
#
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         self.x += other.x
#         self.y += other.y
#         return self  # Ошибка: изменяется текущий объект, а не создаётся новый.
#
#     def __str__(self):
#         return f'Vector({self.x}, {self.y})'
#
#
# if __name__ == '__main__':
#     v1 = Vector(1, 2)
#     v2 = Vector(3, 4)
#     v3 = v1 + v2
#     print(v3)
#     print(v1)
#     print(v1 is v3)

"""
Решение:
Вместо изменения текущего объекта создавайте новый объект.
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'Vector({self.x}, {self.y})'


if __name__ == '__main__':
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    print(v3)
    print(v1)
    print(v1 is v3)