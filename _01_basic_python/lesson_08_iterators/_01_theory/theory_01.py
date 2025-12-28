numbers = [1, 2, 3]  # Итерируемый объект
iterator = iter(numbers)
print(iterator)

# Получаем элементы по одному
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator)) # Ошибка: StopIteration
print()

numbers = [1, 2, 3]
for number in numbers:
    print(number)