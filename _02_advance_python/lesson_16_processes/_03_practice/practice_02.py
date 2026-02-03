"""
Задача 2: Параллельное возведение чисел в степень

Ситуация: мы работаем с большим массивом данных. Для ускорения вычислений,
нам необходимо распараллелить его обработку.

Задача: реализовать программу, которая в нескольких потоках возводит числа
определенного массива в некоторую степень.

- Создайте функцию power_numbers
- Использовать multiprocessing.Queue для передачи данных между процессами.

Шаги реализации:

1) Создайте функцию power_numbers, которая принимает список чисел и степень, в которую нужно возвести эти числа.
2) Разделите исходный список чисел на несколько частей (по количеству процессов).
3) Создайте процессы, каждый из которых будет вызывать функцию power_numbers для своей части данных.
4) Используйте multiprocessing.Queue для передачи результатов от каждого процесса в главный процесс.
5) Соберите результаты из очереди и выведите их.
"""

from multiprocessing import Process, Queue
import random


def power_numbers(numbers, exponent, result_queue):
    results = [num ** exponent for num in numbers]
    result_queue.put(results)


if __name__ == '__main__':
    my_numbers = list(range(1, 21))
    random.shuffle(my_numbers)
    print(my_numbers)
    exponent = 2
    num_processes = 4

    square_queue = Queue()
    chunk_size = len(my_numbers) // num_processes
    processes = []

    for i in range(num_processes):
        start_idx = i * chunk_size  # 0 * 5 = 0 / 1 * 5 = 5

        if i < num_processes - 1:
            end_idx = (i + 1) * chunk_size  # (0 + 1) * 5 = 5 / (1 + 1) * 5 = 10
        else:
            end_idx = len(my_numbers)

        chunk = my_numbers[start_idx: end_idx]

        process = Process(target=power_numbers, args=(chunk, exponent, square_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    all_results = []
    while not square_queue.empty():
        all_results.extend(square_queue.get())

    print(f'Результаты: {all_results}')
