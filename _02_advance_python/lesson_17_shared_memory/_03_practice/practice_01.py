"""
Задача: реализовать программу, в которой два процесса увеличивают общий счётчик.
Счётчик реализуется с помощью объекта Value.
Каждый процесс должен увеличивать значение счётчика 10 раз, синхронизируя доступ к переменной.
"""

from multiprocessing import Value, Lock, Process


def increment_counter(shared_counter: Value, lock: Lock):
    for _ in range(10):
        with lock:
            shared_counter.value += 1


def main():
    my_shared_counter = Value('i', 0)
    my_lock = Lock()

    processes = [Process(target=increment_counter, args=(my_shared_counter, my_lock)) for _ in range(3)]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(f'Итоговое значение счетчика: {my_shared_counter.value}')


if __name__ == '__main__':
    main()
