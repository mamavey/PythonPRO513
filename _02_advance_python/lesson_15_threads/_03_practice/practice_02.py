"""
Задание 2. Синхронизация доступа к общему списку

Ситуация: наш коллега выполнял задачу, подобную прошлой.
Однако в его реализации несколько потоков добавляют данные в общий список.
Необходимо предотвратить гонку данных.

Задачи:

Создать функцию add_to_shared_list, которая добавляет элемент в общий список с использованием Lock.
Запустить 5 потоков, которые добавляют 1000 элементов каждый.
Реализация:
"""

import threading

shared_list = []
lock = threading.Lock()


def add_to_shared_list(item):
    with lock:
        shared_list.append(item)


def worker():
    for i in range(1000):
        add_to_shared_list(i)


if __name__ == '__main__':
    threads = [threading.Thread(target=worker) for i in range(5)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Ожидаемая длина списка: 5000/Фактическая: {len(shared_list)}')
    print(shared_list)