"""
Event Loop
"""
from datetime import datetime
import asyncio


async def task1():
    print('Task1: Start')
    await asyncio.sleep(3)
    print('Task1: End')


async def task2():
    print('Task2: Start')
    await asyncio.sleep(1)
    print('Task2: End')


async def task3():
    print('Task3: Start')
    await asyncio.sleep(2)
    print('Task3: End')


async def main():
    print(datetime.now())
    # Создаём задачи
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    t3 = asyncio.create_task(task3())

    # Ждём завершения всех задач
    await t1
    await t2
    await t3
    print(datetime.now())


if __name__ == '__main__':
    asyncio.run(main())
