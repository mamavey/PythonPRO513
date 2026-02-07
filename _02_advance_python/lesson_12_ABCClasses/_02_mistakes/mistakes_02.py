"""
Тип ошибки 2: Не реализован абстрактный метод в подклассе
Если подкласс не реализует все абстрактные методы, это приведёт к ошибке.
Пример ошибки:
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
# circle = Circle(5)

"""
Решение:

реализуем абстрактный метод в подклассе.
"""


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(5)
print(circle.area())  # 78.5
