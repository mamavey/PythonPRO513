"""
Когда использовать Counter?

- Если нужно быстро подсчитать частоту элементов в коллекции.
- Для обработки текстов (подсчёт слов или символов).
- В задачах анализа данных, где важно понимать распределение элементов.
"""

from collections import Counter

# Подсчет элементов
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
counter = Counter(data)
print(counter)
print()

# Доступ к значениям:
print(counter['banana'])
print(counter['grape'])
print()

# Метод most_common() - возвращает список самых частых элементов в порядке убывания их частоты
# print(counter.most_common())
print(counter.most_common(1))
print(counter.most_common(2))
print()

# Метод update() - позволяет обновить счётчик,
# добавляя новые элементы или увеличивая количество уже существующих.
counter.update(['apple', 'banana', 'grape'])
print(counter)
print()

# Арифметические операции
# сложение, вычитание, пересечение и объединения

# Сложение
c1 = Counter(a=2, b=3)
c2 = Counter(a=1, b=2)
print(c1, c2)
print(c1 + c2)

# Вычитание
print(c1 - c2)
print(c2 - c1)

# Пересечение
c1 = Counter(a=2, b=3)
c2 = Counter(a=1, b=2, c=4)
print(c1 & c2)

c1 = Counter(a=2, b=3)
c2 = Counter(a=1, b=2, c=4)
# Объединение
print(c1 | c2)
