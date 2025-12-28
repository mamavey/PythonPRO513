"""
Тип ошибки 4: Неправильное обращение к статическому методу

Ошибка возникает, если мы пытаемся вызвать статический метод через объект,
как будто это метод экземпляра.

Пример ошибки:
"""

# class MathHelper:
#     @staticmethod
#     def square(num):
#         return num ** 2
#
#
# helper = MathHelper()
# helper.square(4)  # Работает, но статический метод лучше вызывать через класс.


"""
Решение:

Вызовите статический метод через класс:
"""


class MathHelper:
    @staticmethod
    def square(num):
        return num ** 2


print(MathHelper.square(4))
