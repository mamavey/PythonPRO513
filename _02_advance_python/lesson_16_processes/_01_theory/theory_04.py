from multiprocessing import Process, Queue
import time


def compute_square(num, queue):
    result = num ** 2
    print(f'Процесс {num}: вычисление квадрата {num} == {result}')
    queue.put(result)
    time.sleep(1)


if __name__ == '__main__':
    # Создаём очередь для обмена данными
    sqr_queue = Queue()
    processes = []
    # Создаём 4 процесса, каждый будет вычислять квадрат числа от 1 до 4
    for i in range(1, 5):
        process = Process(target=compute_square, args=(i, sqr_queue))
        processes.append(process)
        process.start()

    # Ожидаем завершения всех процессов
    for process in processes:
        process.join()

    # Главный процесс забирает и выводит результаты из очереди
    print('\nРезультаты вычислений: ')
    while not sqr_queue.empty():
        sqr_result = sqr_queue.get()
        print(f'Результат: {sqr_result}')
    print('Все процессы завершены.')
