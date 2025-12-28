"""
Тип ошибки 6: Ошибка в доступе к атрибутам через методы

Ошибка возникает, если мы случайно обращаемся к атрибуту экземпляра,
используя cls в методе класса или наоборот.

Пример ошибки:
"""

# class Car:
#     wheels = 4
#
#     @classmethod
#     def change_color(cls, color):
#         cls.color = color  # Ошибка, цвет относится к объекту, а не классу


"""
Используйте self для атрибутов экземпляра и cls для атрибутов класса:
"""


class Car:
    wheels = 4

    def __init__(self, color):
        self.color = color

    def change_color(self, color):
        self.color = color
