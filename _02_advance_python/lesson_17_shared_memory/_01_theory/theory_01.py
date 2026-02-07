import multiprocessing

"""
Создание значения в разделяемой памяти
"""


# shared_value = multiprocessing.Value('i', 0)
# print(shared_value.value)
# shared_value.value = 42
# print(shared_value.value)

def increment(shared_value):
    for _ in range(10):
        shared_value.value += 1


if __name__ == '__main__':
    my_shared_value = multiprocessing.Value('i', 0)
    process1 = multiprocessing.Process(target=increment, args=(my_shared_value,))
    process2 = multiprocessing.Process(target=increment, args=(my_shared_value,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()
    print(f'Итоговое значение: {my_shared_value.value}')
