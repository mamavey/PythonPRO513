"""race condition (гонка данных) пример 2"""
import threading
from datetime import datetime

counter = 0


def increment(lock):
    global counter

    for i in range(10000000):
        # result = get_value()
        with lock:
            counter += 1


# def get_value():
#     return 1


if __name__ == '__main__':
    print(datetime.now())
    lock_obj = threading.Lock()
    threads = []
    for _ in range(5):
        threads.append(threading.Thread(target=increment, args=(lock_obj,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Counter value: {counter}')
    print(datetime.now())
