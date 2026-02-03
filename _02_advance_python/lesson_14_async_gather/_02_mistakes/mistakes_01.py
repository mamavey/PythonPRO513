"""
Тип ошибки 1: Некорректная распаковка задач в asyncio.gather

Ошибка возникает, когда задачи передаются в gather в виде списка без распаковки.

Пример ошибки:
"""
import asyncio

# async def task():
#     await asyncio.sleep(1)

#
# async def main():
#     tasks = [task(), task(), task()]
#     await asyncio.gather(tasks)  # Ошибка: передача списка без распаковки
#
#
# asyncio.run(main())

"""
Решение:

используем оператор * для распаковки списка задач.
"""


async def task():
    await asyncio.sleep(1)


async def main():
    tasks = [task(), task(), task()]
    await asyncio.gather(*tasks)
