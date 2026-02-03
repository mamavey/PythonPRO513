"""
Тип ошибки 3: Передача не awaitable объектов
Ошибка возникает при передаче в gather объектов, которые не являются корутинами или задачами.

Пример ошибки:
"""

import asyncio

# def sync_function():
#     return 42
#
#
# async def main():
#     await asyncio.gather(sync_function())  # Ошибка: функция не является корутиной
#
#
# asyncio.run(main())


"""
Решение:

обернём синхронную функцию в корутину.
"""


def sync_function():
    return 42


async def wrapper(func):
    return func()


async def main():
    await asyncio.gather(wrapper(sync_function))


asyncio.run(main())
