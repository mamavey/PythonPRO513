import sys

# Создание списка квадратов чисел от 0 до 4
squares = [x ** 2 for x in range(5)]  # генераторное выражение (но не генератор как объект).
print(squares)  # Вывод: [0, 1, 4, 9, 16]

# Создание словаря, где ключи — это числа, а значения — их квадраты
squares_dict = {x: x ** 2 for x in range(5)}
print(squares_dict)

# Создание множества квадратов чисел
squares_set = {x ** 2 for x in range(5)}
print(squares_set)

# Список только чётных чисел от 0 до 9
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

even_nums = []
for x in range(10):
    if x % 2 == 0:
        even_nums.append(x)
print(even_nums)

# Словарь только для квадратов нечётных чисел
odd_squares_dict = {x: x ** 2 for x in range(10) if x % 2 != 0}
print(odd_squares_dict)
# print(sys.getsizeof(odd_squares_dict))

odd_squares = {}
for x in range(10):
    if x % 2 != 0:
        odd_squares[x] = x ** 2
print(odd_squares)
