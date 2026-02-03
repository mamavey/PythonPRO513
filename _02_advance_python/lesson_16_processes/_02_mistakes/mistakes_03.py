"""
Тип ошибки 3: Игнорирование ошибок в дочерних процессах
Если в дочернем процессе возникает ошибка, она может остаться незамеченной,
и основной процесс продолжит работу, не зная о сбое.
"""
from multiprocessing import Process


# def task():
#     print("Процесс начал работу.")
#     1 / 0  # Исключение в дочернем процессе
#     print("Процесс завершен.")
#
#
# if __name__ == "__main__":
#     process = Process(target=task)
#     process.start()
#     process.join()
#     print("Основной процесс завершен.")

"""
Решение:
логируем ошибки в дочерних процессах и передаём их в основной процесс через очередь или другие механизмы IPC. 
Пример с передачей ошибок через Queue:
"""
from multiprocessing import Process, Queue


def task(queue):
    try:
        print("Процесс начал работу.")
        1 / 0  # Исключение в дочернем процессе
    except Exception as e:
        queue.put(str(e))  # Отправляем ошибку в очередь


if __name__ == "__main__":
    queue = Queue()
    process = Process(target=task, args=(queue,))
    process.start()
    process.join()

    # Проверяем на наличие ошибок
    if not queue.empty():
        error_message = queue.get()
        print(f"Ошибка в процессе: {error_message}")
    else:
        print("Процесс завершился успешно.")
