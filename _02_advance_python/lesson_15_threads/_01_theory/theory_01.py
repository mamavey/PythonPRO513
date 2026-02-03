import threading
import time


def print_numbers():
    for i in range(10):
        print(f'Number: {i}')
        time.sleep(1.0)


if __name__ == '__main__':
    # Создаём поток
    thread = threading.Thread(target=print_numbers)
    thread.start()
    # Основной поток продолжает выполнять свои задачи
    print('Поток запущен')
    time.sleep(2.0)
    print('Поток в процессе работы...')
    # Ждём, пока поток завершится
    thread.join()
    print('Поток завершен')
