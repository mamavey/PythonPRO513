"""
Тип ошибки 3: Неправильное использование join()

Ошибка возникает, когда join() вызывается до start(), что приводит к блокировке основного потока.
"""

import threading


# def worker():
#     print("Working...")
#
#
# thread = threading.Thread(target=worker)
# thread.join()  # Ошибка: join() перед start()
# thread.start()

"""
Решение:

всегда вызываем start() перед join().
"""


def worker():
    print("Working...")


thread = threading.Thread(target=worker)
thread.start()
thread.join()
