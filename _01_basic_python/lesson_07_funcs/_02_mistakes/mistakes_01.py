"""
Типичные ошибки
Тип ошибки 1: Вызов функции до её определения — NameError: name ‘greet’ is not defined
Ошибка возникает, если вызвать функцию до ее определения.
Пример ошибки:
"""

# greet("Alice")
#
#
# def greet(name):
#     print(f"Hello, {name}!")


"""
Решение:

Всегда определяйте функции перед их вызовом.
"""

def greet(name):
    print(f"Hello, {name}!")


greet("Alice")

