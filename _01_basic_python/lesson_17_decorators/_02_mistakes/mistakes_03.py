"""
Тип ошибки 3: Потеря имени функции из-за декоратора
Если декоратор не использует functools.wraps, имя и документация исходной функции будут потеряны.
"""

# def decorator(func):
#     def wrapper():
#         print("Обёртка")
#         func()
#
#     return wrapper
#
#
# @decorator
# def greet():
#     """Функция приветствия."""
#     print("Привет!")
#
#
# print(greet.__name__)  # Вывод: wrapper (а не greet)
# print(greet.__doc__)  # None


"""
Решение:
"""

from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper():
        print("Обёртка")
        func()

    return wrapper


@decorator
def greet():
    """Функция приветствия."""
    print("Привет!")


print(greet.__name__)  # Вывод: greet
print(greet.__doc__)  # Функция приветствия.
