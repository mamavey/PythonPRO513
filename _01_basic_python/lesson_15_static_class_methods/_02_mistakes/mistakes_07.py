"""
Тип ошибки 7: Избыточное использование self или cls
Ошибка возникает, если мы используем self или cls, где это не нужно, например, в статическом методе.

Пример ошибки:
"""

# class MathHelper:
#
#     @staticmethod
#     def square(self, num):  # Ошибка: self не нужен
#         return num ** 2
#

"""
Используйте self для атрибутов экземпляра и cls для атрибутов класса:
"""

class MathHelper:

    @staticmethod
    def square(num):
        return num ** 2

