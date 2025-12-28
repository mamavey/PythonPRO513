"""
Тип ошибки 2: Неправильное количество аргументов — TypeError: add() missing 1 required positional argument
Пример ошибки:
"""
# def add(a, b):
#     return a + b
#
#
# result = add(5)  # Пропущен второй аргумент



"""
Решение:

Убедитесь, что передаёте все обязательные аргументы, или используйте значения по умолчанию.
"""

def add(a, b=0):
    return a + b


result = add(5)  # Работает: 5 + 0 = 5
print(result)
