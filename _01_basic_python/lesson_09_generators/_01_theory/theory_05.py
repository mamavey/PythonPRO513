def numbers_generator(limit):
    for x in range(limit):
        yield x ** 2


if __name__ == '__main__':
    numbers_gen_1 = (x ** 2 for x in range(5))  # Генератор квадратов чисел]
    print(numbers_gen_1)
    print(next(numbers_gen_1))
    print(next(numbers_gen_1))
    print(next(numbers_gen_1))
    print(list(numbers_gen_1))
    print()

    numbers_gen_2 = numbers_generator(5)
    print(numbers_gen_2)
    print(next(numbers_gen_2))
    print(next(numbers_gen_2))
    print(next(numbers_gen_2))
    print(list(numbers_gen_2))
