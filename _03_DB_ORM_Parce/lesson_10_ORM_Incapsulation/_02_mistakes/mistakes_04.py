"""
Тип ошибки 4: Избыточное использование геттеров и сеттеров
Создание геттеров и сеттеров для всех атрибутов, даже если они не нужны,
усложняет код и делает его менее читаемым.
Пример ошибки:
"""


class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    # @name.setter
    # def name(self, value):
    #     self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


"""
Решение:
Использовать геттеры и сеттеры только при необходимости:
"""


class User:
    def __init__(self, name, age):
        self.name = name  # Публичный атрибут
        self.age = age  # Публичный атрибут
