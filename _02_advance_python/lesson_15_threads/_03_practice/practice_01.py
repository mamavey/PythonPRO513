"""
Задание 1. Пул потоков с ограничением на одновременное выполнение

Ситуация: нам поставили задачу оптимизировать работу нашего проекта с сетью.
Для этого необходимо реализовать систему, которая обрабатывает до трёх задач одновременно.

Задача:

Создать класс ThreadPool, который:
инициализируется с максимальным количеством потоков;
добавляет задачи в очередь и запускает их при наличии свободных потоков;
использует queue.Queue для хранения задач и threading.Thread для их выполнения,
при этом ограничивает количество одновременно выполняемых потоков.
"""
import threading
from threading import Thread, Lock
from queue import Queue
import time
import random


class ThreadPool:
    def __init__(self, max_threads):
        self.max_threads = max_threads
        self.task_queue = Queue()
        self.running_threads = 0

    def add_task(self, task_func, *args):
        self.task_queue.put((task_func, args))
        self._try_run_task()

    def _worker(self):
        if not self.task_queue.empty():  # чтобы программа завершалась сама
            task_func, args = self.task_queue.get()
            task_func(*args)
            self.task_queue.task_done()

            # после завершения задачи уменьшаем количество работающих потоков
            with Lock():
                self.running_threads -= 1

            # попробуем запустить следующую задачу, если есть свободные потоки
            self._try_run_task()

    def _try_run_task(self):
        # если количество работающих потоков меньше максимального, запускаем новый
        if self.running_threads < self.max_threads:
            with threading.Lock():
                self.running_threads += 1
            threading.Thread(target=self._worker).start()


def process_task(task_id):
    print(f'Начало обработки задачи: {task_id}')
    time.sleep(random.randint(1, 3))
    print(f'Завершение задачи: {task_id}')


if __name__ == '__main__':
    pool = ThreadPool(3)
    for i in range(1, 10):
        pool.add_task(process_task, i)
