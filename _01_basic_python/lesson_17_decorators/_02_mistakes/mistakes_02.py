"""
Тип ошибки 2: Неправильное использование декоратора — TypeError: ‘function’ object is not callable

Если декоратор принимает аргументы, но используется как обычный декоратор, это вызовет ошибку.
"""

# def repeat(n):
#     def decorator(func):
#         def wrapper():
#             for _ in range(n):
#                 func()
#         return wrapper
#     return decorator
#
# @repeat  # Пропустили скобки и аргумент
# def greet():
#     print("Привет!")
#
# greet()


"""
Решение: передать параметр в декоратор
"""

# def repeat(n):
#     def decorator(func):
#         def wrapper():
#             for _ in range(n):
#                 func()
#
#         return wrapper
#
#     return decorator
#
#
# @repeat(3)  # Пропустили скобки и аргумент
# def greet():
#     print("Привет!")
#
#
# greet()
