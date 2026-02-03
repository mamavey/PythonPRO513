"""
is_alive() проверяет, работает ли процесс в данный момент;
terminate() завершает процесс принудительно.
"""
import multiprocessing
import time


def long_task():
    print('Процесс начал работу.')
    time.sleep(5)
    print('Процесс завершил работу.')


if __name__ == '__main__':
    process = multiprocessing.Process(target=long_task)
    process.start()

    time.sleep(2)
    # Проверяем, работает ли процесс
    if process.is_alive():
        print(f'Процесс все еще работает, прерываем его')
        process.terminate()  # Принудительно завершаем процесс

    process.join()  # Дожидаемся завершения процесса
    print('Процесс завершен')
