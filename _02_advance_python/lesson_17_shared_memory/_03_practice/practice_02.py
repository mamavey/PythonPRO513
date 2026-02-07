"""
Задача: реализовать программу, в которой массив чисел (Array) заполняется несколькими процессами.
Каждый процесс добавляет квадрат своего индекса в общий массив.
Использовать синхронизацию для защиты массива от одновременного изменения.
"""

from multiprocessing import Array, Lock, Process


def fill_array(shared_array: Array, index, lock: Lock):
    with lock:
        shared_array[index] = index ** 2
        print(f'Процесс {index}: записано {index ** 2}')


def main():
    size = 5
    my_shared_array = Array('i', size)
    my_lock = Lock()

    processes = [Process(target=fill_array, args=(my_shared_array, i, my_lock)) for i in range(size)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(f'Итоговый массив: {list(my_shared_array)}')


if __name__ == '__main__':
    main()
