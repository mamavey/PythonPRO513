import sys


def create_nums_list(limit):
    nums_list = []
    for x in range(limit):
        nums_list.append(x ** 2)
    return nums_list


numbers_list = [x ** 2 for x in range(1000)]  # Список квадратов чисел (списковое выражение/list comprehension)


def numbers_generator(limit):
    for x in range(limit):
        yield x ** 2


numbers_gen = (x ** 2 for x in range(1000))  # Генератор квадратов чисел

print(f'Размер списка: {sys.getsizeof(numbers_list)} байт')
print(f'Размер генератора: {sys.getsizeof(numbers_gen)} байт')
