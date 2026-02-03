from multiprocessing import Pool
from platform import platform, machine, processor, system, version


def square(x):
    return x ** 2


if __name__ == '__main__':
    # print(platform(aliased=False, terse=False))
    # print(platform(aliased=True, terse=False))
    # print(platform(aliased=False, terse=True))
    # print(machine())
    print(processor())
    # print(system())
    # print(version())
    user_pc = {
        "AMD64 Family 25 Model 33 Stepping 2, AuthenticAMD": {'cores': 8, 'threads': 16}
    }
    cores = user_pc[processor()]['cores']
    print(cores)
    with Pool(processes=cores) as pool:
        # Список чисел для обработки
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        # Применяем функцию ко всем элементам с помощью map
        results = pool.map(square, numbers)

    print(f'Квадраты чисел: {results}')
