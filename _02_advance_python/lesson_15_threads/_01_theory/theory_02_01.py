import threading
import time

counter = 0


def increase(by):
    global counter  # так делать не стоит

    local_counter = counter
    local_counter += by

    time.sleep(0.5)
    counter = local_counter
    print(f'Значение counter: {counter}')


if __name__ == '__main__':
    # Создаём поток
    thread1 = threading.Thread(target=increase, args=(10,))
    thread2 = threading.Thread(target=increase, args=(20,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f'Итоговое значение counter: {counter}')
