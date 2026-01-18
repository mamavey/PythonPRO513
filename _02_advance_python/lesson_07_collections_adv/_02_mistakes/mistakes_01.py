"""
Тип ошибки 1: Ограничение длины deque

Старые элементы неожиданно удаляются при добавлении новых.

Пример ошибки:
"""
from collections import deque

d = deque([1, 2, 3], maxlen=3)
print(deque)
d.append(5)
print(d)

"""
Решение:
убедимся, что длина задаётся правильно.
"""

d = deque(maxlen=4)
d.append(1)
d.append(2)
d.append(3)
d.append(4)
print(d)
