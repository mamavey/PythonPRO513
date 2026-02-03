from multiprocessing import Process, Pipe
import time


def sender(conn):
    for i in range(1, 6):
        print(f'Отправитель отправляет: {i}')
        conn.send(i)  # Отправляем данные через канал
        time.sleep(1)
    conn.send("DONE")


def receiver(conn):
    while True:
        data = conn.recv()  # Получаем данные из канала
        if data == 'DONE':
            break
        print(f'Получатель получил: {data}')


if __name__ == '__main__':
    # Создаём канал связи
    parent_conn, child_conn = Pipe()

    # Запускаем два процесса: производитель и потребитель
    sender_process = Process(target=sender, args=(parent_conn,))
    receiver_process = Process(target=receiver, args=(child_conn,))

    sender_process.start()
    receiver_process.start()

    # Ожидаем завершения процессов
    sender_process.join()
    # Отправляем сигнал завершения для потребителя
    # parent_conn.send('DONE')
    receiver_process.join()

    print('Обмен данными завершен')
