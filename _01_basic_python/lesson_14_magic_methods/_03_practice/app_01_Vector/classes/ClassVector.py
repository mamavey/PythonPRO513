"""
Задача: создайте класс Vector2D, который:

Имеет атрибуты:
x — координата по оси X.
y — координата по оси Y.
Использует следующие методы:
__add__: складывает два вектора.
__sub__: вычитает один вектор из другого.
__str__: возвращает строковое представление вектора.
__len__: возвращает длину вектора (округлённую до ближайшего целого числа).
length: вычисляет длину вектора.
angle: вычисляет угол вектора относительно оси X.
"""

import math


class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError(
                f'{type(other).__name__} != {type(self).__name__} >> Оба объекта должны принадлежать у к классу: {type(self).__name__}'
            )
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if not isinstance(other, Vector2D):
            raise TypeError(
                f'{type(other).__name__} != {type(self).__name__} >> Оба объекта должны принадлежать у к классу: {type(self).__name__}'
            )
        return Vector2D(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f'Vector2D({self.x}, {self.y})'

    def __len__(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2))

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def angle(self):
        return math.degrees(math.atan2(self.y, self.x))

    # @staticmethod
    # def instance_check(obj, cls):
    #     if not isinstance(obj, cls):
    #         raise TypeError(
    #             f"{type(obj).__name__} != {cls.__name__} >> Оба объекта должны принадлежать к классу: {cls.__name__}")
    #     return True
