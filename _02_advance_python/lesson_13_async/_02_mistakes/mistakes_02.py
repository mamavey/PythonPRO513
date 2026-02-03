"""
Тип ошибки 2: Некорректное использование asyncio.run

Ошибка возникает, когда asyncio.run вызывается внутри другой корутины.
"""

import asyncio


async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)  # Ошибка: забыли await
    print("End")


# async def main():
#     asyncio.run(my_coroutine())  # Ошибка: asyncio.run нельзя вызывать внутри корутины


"""
Решение: правильно использовать await
"""


async def main():
    await my_coroutine()


if __name__ == '__main__':
    asyncio.run(main())
