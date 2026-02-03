import threading
from time import sleep


class Counter:

    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increase(self, by):
        with self.lock:
            current_value = self.value
            current_value += by
            sleep(0.5)
            self.value = current_value
            print(f'Значение value: {self.value}')


if __name__ == '__main__':
    counter = Counter()
    threads = [threading.Thread(target=counter.increase, args=(i,)) for i in range(10, 31, 10)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f'Значение value в итоге: {counter.value}')
