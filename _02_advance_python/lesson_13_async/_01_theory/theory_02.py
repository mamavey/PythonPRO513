"""
Корутина
"""
import asyncio


async def my_coroutine():
    print('Start')
    await asyncio.sleep(1)  # Приостанавливаем выполнение на 1 секунду
    print('End')


if __name__ == '__main__':
    # Запуск корутины
    asyncio.run(my_coroutine())
