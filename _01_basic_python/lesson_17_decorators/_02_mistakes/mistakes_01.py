"""
Тип ошибки 1: Декоратор не возвращает функцию — TypeError: ‘NoneType’ object is not callable

Если забыть вернуть функцию-обертку из декоратора, он не будет работать.
"""

# def decorator(func):
#     def wrapper():
#         print("Декоратор работает")
#         func()
#     # Здесь забыли return wrapper
#
#
# @decorator
# def say_hello():
#     print("Привет!")
#
#
# say_hello()

"""
Решение: возвращаем обертку из декоратора
"""


def decorator(func):
    def wrapper():
        print("Декоратор работает")
        func()

    return wrapper


@decorator
def say_hello():
    print("Привет!")


say_hello()
