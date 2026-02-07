"""
Задача: реализовать программу,
в которой несколько процессов обрабатывают массив данных (Array) и подсчитывают сумму его элементов.
Каждый процесс обрабатывает свою часть массива. Общий результат сохраняется в объект Value с синхронизацией доступа.
"""

from multiprocessing import Value, Array, Process, Lock


def compute_partial_sum(sh_array, start, end, sh_sum, lock):
    local_sum = sum(sh_array[start: end])  # Подсчёт суммы части массива
    print(f'Частичная сумма индексы значений от и до (не включая) ({start}-{end}: {local_sum})')  # используются индексы значений
    # print(f'Частичная сумма ({start + 1}-{end}: {local_sum})')  # используются сами значения
    with lock:
        sh_sum.value += local_sum


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8]  # Исходный массив
    shared_array = Array('i', data)  # Разделяемый массив
    shared_sum = Value('i', 0)  # Разделяемая сумма
    my_lock = Lock()

    num_processes = 4
    chunk_size = len(data) // num_processes  # 8 / 4 = 2
    processes = []

    for i in range(num_processes):  # 0             |1
        start = i * chunk_size  # start = 0 * 2 |start = 1 * 2
        if i != num_processes - 1:  # 0 != 3        |1 != 3
            end = start + chunk_size  # end = 0 + 2   |end = 2 + 2
        else:  # [0:2]         |[2:4]
            end = len(data)

        process = Process(target=compute_partial_sum, args=(shared_array, start, end, shared_sum, my_lock))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(f'Общая сумма элементов массива: {shared_sum.value}')


if __name__ == '__main__':
    main()
