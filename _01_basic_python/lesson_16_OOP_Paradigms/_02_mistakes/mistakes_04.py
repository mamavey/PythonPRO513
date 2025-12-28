"""
Тип ошибки 4: Отсутствие реализации абстрактного метода

Ошибка возникает, когда класс наследуется от абстрактного класса,
но не реализует все его абстрактные методы.
Такой класс сам становится абстрактным и не может быть инициализирован.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# class Circle(Shape):
#     pass  # Ошибка: метод area не реализован
#
# circle = Circle()  # TypeError: Can't instantiate abstract class Circle


"""
Решение:

Обязательно реализуйте все абстрактные методы в дочернем классе.
"""


class Circle(Shape):
    def area(self):
        return 3.14 * 5 ** 2


circle = Circle()
