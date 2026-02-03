"""
Тип ошибки 4: Бесконечные создание процессов

Ошибка возникает, когда процессы создаются в основном теле программы (вне блока if __name__ == '__main__':).
"""
# from multiprocessing import Process
#
#
# def task():
#     print("Процесс работает.")
#
#
# process = Process(target=task)
# process.start()
# process.join()

"""
Решение:
Оборачиваем код создания процессов в блок if __name__ == '__main__':.
"""

from multiprocessing import Process


def task():
    print("Процесс работает.")


if __name__ == '__main__':
    process = Process(target=task)
    process.start()
    process.join()