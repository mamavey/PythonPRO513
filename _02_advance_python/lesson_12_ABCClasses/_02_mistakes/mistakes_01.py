"""
Тип ошибки 1: Попытка инстанцировать абстрактный класс
Абстрактные классы не могут быть инстанцированы напрямую. Попытка сделать это приведёт к ошибке.
Пример ошибки:
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


# animal = Animal()  # Ошибка: TypeError: Can't instantiate abstract class Animal with abstract method make_sound

"""
Решение:
создаём подкласс и реализуем абстрактные методы.
"""


class Dog(Animal):
    def make_sound(self):
        return "Гав!"


dog = Dog()
print(dog.make_sound())  # Гав!

