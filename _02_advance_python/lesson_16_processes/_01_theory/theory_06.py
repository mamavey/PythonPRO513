from multiprocessing import Pool


def square(x):
    return x ** 2


if __name__ == '__main__':
    # Создаём пул из 4 процессов
    with Pool(processes=4) as pool:
        # Список чисел для обработки
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]

        # Применяем функцию ко всем элементам с помощью map
        results = pool.map(square, numbers)

    print(f'Квадраты чисел: {results}')
