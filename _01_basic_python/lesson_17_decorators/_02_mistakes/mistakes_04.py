"""
Тип ошибки 4: Аргументы декорируемой функции не учтены
Если функция принимает аргументы, но декоратор их не обрабатывает, это вызовет ошибку.
"""
#
# def decorator(func):
#     def wrapper():
#         print("Обёртка")
#         func()  # Здесь нет передачи аргументов
#
#     return wrapper
#
#
# @decorator
# def add(a, b):
#     print(a + b)
#
#
# add(3, 4)  # Ошибка: TypeError


"""
Решение: использовать *args и **kwargs в обертке (wrapper)
"""


def decorator(func):
    def wrapper(*args, **kwargs):
        print("Обёртка")
        func(*args, **kwargs)

    return wrapper


@decorator
def add(a, b):
    print(a + b)


add(3, 4)
