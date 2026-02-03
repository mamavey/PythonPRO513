import threading
import queue
import time


# Функция, которую будут выполнять воркеры
def worker(q):
    while not q.empty():  # Пока в очереди есть задачи
        task = q.get()  # Извлекаем задачу из очереди
        print(f'Processing: {task}')
        time.sleep(1)  # Имитируем выполнение задачи
        q.task_done()  # Сообщаем, что задача выполнена


if __name__ == '__main__':
    # Создаём очередь и заполняем задачами
    my_q = queue.Queue()
    for i in range(1, 10):
        my_q.put(f'Task: {i}')

    # Запускаем несколько потоков-воркеров
    threads = [threading.Thread(target=worker, args=(my_q, )) for _ in range(3)]

    for thread in threads:
        thread.start()

    # Ждём, пока все задачи не будут завершены (вместо завершения потоков по отдельности).
    my_q.join()
    print(f'All tasks are proceed.')
