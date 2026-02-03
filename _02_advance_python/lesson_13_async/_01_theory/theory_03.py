"""
Создание Task
"""

import asyncio


async def my_coroutine(sleep_time):
    print(f'Start {sleep_time}')
    await asyncio.sleep(sleep_time)  # Приостанавливаем выполнение на 1 секунду
    print(f'End {sleep_time}')


async def main():
    # Создаём таску из корутины
    task1 = asyncio.create_task(my_coroutine(3))
    task2 = asyncio.create_task(my_coroutine(1))
    # Ждём завершения таски
    await task1
    await task2


if __name__ == '__main__':
    # Запуск Task
    asyncio.run(main())
