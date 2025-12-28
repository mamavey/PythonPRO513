"""
Тип ошибки 3: Отсутствие проверки типов в методе __add__
Если попытаться сложить объект класса с несоответствующим типом, Python выбросит ошибку.

Пример ошибки:
"""
# class Vector:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)  # Ошибка, если other не является объектом Vector.
#
#     def __str__(self):
#         return f'Vector({self.x}, {self.y})'
#
#
# if __name__ == '__main__':
#     v1 = Vector(1, 2)
#     v2 = "Vector(3, 4)"
#     v3 = v1 + v2
#     print(v3)

"""
Решение:
Добавьте проверку типа для аргумента other в методе __add__.
"""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Сложение возможно только между объектами класса Vector")
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f'Vector({self.x}, {self.y})'


if __name__ == '__main__':
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    # v2 = "Vector(3, 4)"
    v3 = v1 + v2
    print(v3)
