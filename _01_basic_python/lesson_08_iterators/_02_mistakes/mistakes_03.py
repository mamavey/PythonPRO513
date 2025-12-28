"""
Тип ошибки 3: Использование итератора в другой части программы

Итератор «запоминает», где мы остановились, поэтому, если мы передадим итератор в другую часть программы,
элементы могут быть пропущены или повторно недоступны.
"""

numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)

for _ in range(3):
    try:
        print(next(iterator))
    except StopIteration:
        break

print("Что делаем, при этом ожидая что итератор начнется с 1го элемента")

for _ in range(3):
    try:
        print(next(iterator))
    except StopIteration:
        break
print()


"""
Решение:

Создавайте новый итератор, если он нужен в другой части программы.
"""

numbers = [1, 2, 3, 4, 5]
iterator1 = iter(numbers)

for _ in range(3):
    try:
        print(next(iterator1))
    except StopIteration:
        break

print("Что делаем, при этом ожидая что итератор начнется с 1го элемента")

iterator2 = iter(numbers)
for _ in range(3):
    try:
        print(next(iterator2))
    except StopIteration:
        break


