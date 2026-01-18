"""
Задание 1. Очередь обработки задач с ограничением

Ситуация: мы создаём систему обработки задач,
где одновременно можно хранить только последние 5 задач для обработки.
Если добавляется новая, самая старая автоматически удаляется.
Нам нужно реализовать эту систему с использованием deque.

Задача — создать класс TaskQueue, который:

- Инициализируется с максимальной длиной очереди.
- Имеет метод add_task(task), который добавляет новую задачу в очередь.
- Имеет метод get_tasks(), который возвращает список текущих задач.

Используем deque с параметром maxlen для реализации.

Шаги реализации:

- Создадим класс TaskQueue и инициализируем его объектом deque с заданной максимальной длиной.
- Реализуем метод add_task(task) для добавления задач.
- Реализуем метод get_tasks() для получения всех текущих задач в очереди.
"""
from collections import deque


class TaskQueue:
    def __init__(self, max_length):
        self.queue = deque(maxlen=max_length)

    def add_task(self, task):
        self.queue.append(task)

    def add_important_task(self, task):
        self.queue.appendleft(task)

    def get_tasks(self):
        return list(self.queue)


if __name__ == '__main__':
    tq = TaskQueue(4)
    tq.add_task('task1')
    tq.add_task('task2')
    tq.add_task('task3')
    tq.add_task('task4')
    print(tq.get_tasks())
    tq.add_important_task('task0')
    print(tq.get_tasks())
