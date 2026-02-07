from multiprocessing import Process, Array

"""
Создание массива в разделяемой памяти.
"""
import random


# shared_array = Array('i', 5)  # Массив целых чисел длиной 5
# # Первый аргумент — тип элементов массива (аналогично Value).
# # Второй аргумент — итерируемый объект (список) или размер массива.

def square_elements(shared_array):
    for i in range(len(shared_array)):
        shared_array[i] = shared_array[i] ** 2


if __name__ == '__main__':
    # Создание массива на основе большого списка и известного количества процессов.
    my_list = [1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(my_list)
    mid_idx = len(my_list) // 2  # 4
    first_part = my_list[:4]
    second_part = my_list[4:]
    my_shared_array1 = Array('i', first_part)
    my_shared_array2 = Array('i', second_part)

    # Работа с созданием, запуском и ожиданием завершения процессов.
    process1 = Process(target=square_elements, args=(my_shared_array1, ))
    process2 = Process(target=square_elements, args=(my_shared_array2, ))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print(f'Итоговый массив: {list(my_shared_array1)}')
    print(f'Итоговый массив: {list(my_shared_array2)}')
