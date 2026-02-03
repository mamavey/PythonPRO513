from multiprocessing import Process, Queue
import time


def producer(queue: Queue):
    for i in range(1, 6):
        print(f'Производитель отправил: {i}')
        queue.put(i)  # Помещаем данные в очередь
        time.sleep(1)
    queue.put('DONE')


def consumer(queue: Queue):
    while True:
        item = queue.get()
        if item == 'DONE':
            break
        print(f'Потребитель получил: {item}')


if __name__ == '__main__':
    my_queue = Queue()  # Создаём очередь

    # Запускаем два процесса: производитель и потребитель
    producer_process = Process(target=producer, args=(my_queue,))
    consumer_process = Process(target=consumer, args=(my_queue,))

    producer_process.start()
    consumer_process.start()

    # Ожидаем завершения процессов
    producer_process.join()
    # Отправляем сигнал завершения для потребителя
    # my_queue.put('DONE')
    consumer_process.join()

    print('Обмен данными завершен.')