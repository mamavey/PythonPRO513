"""
Тип ошибки 2: Недостаточное управление ресурсами
Ошибка возникает при создании большого количества процессов.
Это может привести к исчерпанию ресурсов системы (например, памяти или времени процессора).
"""

from multiprocessing import Process
import time

#
# def long_task():
#     print("Долгая задача выполняется.")
#     time.sleep(2)
#     print("Долгая задача выполена.")
#
#
# if __name__ == "__main__":
#     processes = []
#     for _ in range(10000):  # Попытка создать много процессов
#         process = Process(target=long_task)
#         processes.append(process)
#         process.start()
#
#     for process in processes:
#         process.join()


"""
Решение:
используем пул процессов Multiprocessing.Pool для управления количеством одновременно работающих процессов.
"""

from multiprocessing import Pool


def long_task(x):
    print(f"Долгая задача выполняется для {x}")


if __name__ == "__main__":
    with Pool(4) as pool:  # Ограничиваем количество одновременно работающих процессов
        pool.map(long_task, range(100))  # Выполняем задачу для нескольких значений