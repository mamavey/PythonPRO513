"""race condition (гонка данных) пример 2"""
import threading

counter = 0


def increment():
    global counter

    for i in range(100000):
        counter += 1


if __name__ == '__main__':
    threads = []
    for _ in range(5):
        threads.append(threading.Thread(target=increment))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Counter value: {counter}')
    # Counter value: 432157
