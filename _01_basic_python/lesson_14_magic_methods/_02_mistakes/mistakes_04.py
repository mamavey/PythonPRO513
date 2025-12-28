"""
Тип ошибки 4: Некорректная реализация __eq__

Возникает, когда метод __eq__ сравнивает не все атрибуты или использует некорректную логику.

Пример ошибки:
"""
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __eq__(self, other):
#         return self.name == other.name  # Ошибка: сравнивается только имя, возраст игнорируется.

"""
Решение:
Сравнивайте все значимые атрибуты объекта.
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
