"""
Тип ошибки 2: Deadlock (Взаимная блокировка)

Ошибка возникает, когда два или более потока блокируют друг друга, ожидая освобождения ресурсов.
"""

import threading

# lock1 = threading.Lock()
# lock2 = threading.Lock()
#
#
# def thread1():
#     with lock1:
#         with lock2:
#             print("Thread 1")
#
#
# def thread2():
#     with lock2:
#         with lock1:
#             print("Thread 2")
#
#
# t1 = threading.Thread(target=thread1)
# t2 = threading.Thread(target=thread2)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

"""
Решение:
упорядочиваем захват блокировок в одинаковом порядке.
"""

lock1 = threading.Lock()
lock2 = threading.Lock()


def thread1():
    with lock1:
        with lock2:
            print("Thread 1")


def thread2():
    with lock1:
        with lock2:
            print("Thread 2")


t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()
