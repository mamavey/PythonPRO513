import threading
import time

counter = 0


# def increase(by, lock):
#     global counter  # так делать не стоит
#
#     lock.acquire()
#     local_counter = counter
#     local_counter += by
#     time.sleep(0.5)
#     counter = local_counter
#     print(f'Значение counter: {counter}')
#     lock.release()

def increase(by, lock):
    global counter
    with lock:
        local_counter = counter
        local_counter += by
        time.sleep(0.5)
        counter = local_counter
        print(f'Значение counter: {counter}')


if __name__ == '__main__':
    my_lock = threading.Lock()
    # Создаём поток
    thread1 = threading.Thread(target=increase, args=(10, my_lock))
    thread2 = threading.Thread(target=increase, args=(20, my_lock))
    thread3 = threading.Thread(target=increase, args=(30, my_lock))

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()

    print(f'Итоговое значение counter: {counter}')
