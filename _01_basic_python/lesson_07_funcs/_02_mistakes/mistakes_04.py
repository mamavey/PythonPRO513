"""
Тип ошибки 4: Переопределение импортированной функции — TypeError: ‘str’ object is not callable

Пример ошибки:
"""

# from math import sqrt
#
# sqrt = "Not a function"  # Переопределение имени функции
# print(sqrt(16))


"""
Решение:

Не используйте имена встроенных или импортированных функций для переменных.
"""

from math import sqrt
from math import sqrt as sqrt_  # (или используйте псевдонимы)

print(sqrt(16))  # Работает корректно
