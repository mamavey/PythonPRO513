"""
Тип ошибки 2: Пропущенное исключение StopIteration
Ошибка возникает, если вручную вызывать next() и элементы итератора заканчиваются,
Python выбросит исключение StopIteration. Это может завершить программу с ошибкой,
если исключение не обработано.
"""

# numbers = [1, 2, 3]
# iterator = iter(numbers)
#
# print(next(iterator))  # Вывод: 1
# print(next(iterator))  # Вывод: 2
# print(next(iterator))  # Вывод: 3
# print(next(iterator))  # Ошибка: StopIteration


"""
Решение:

Используйте блок try-except, чтобы обработать исключение StopIteration.
"""

numbers = [1, 2, 3]
iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break  # Выходим из цикла, когда элементы заканчиваются
