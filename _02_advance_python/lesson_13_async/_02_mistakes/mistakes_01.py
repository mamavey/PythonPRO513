"""
Тип ошибки 1: Забываем await

Ошибка возникает, когда забываем использовать await перед вызовом асинхронной функции.
"""

import asyncio


# async def my_coroutine():
#     print("Start")
#     asyncio.sleep(1)  # Ошибка: забыли await
#     print("End")

"""
Решение: не забываем про await
"""

async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)  # Ошибка: забыли await
    print("End")


if __name__ == '__main__':
    asyncio.run(my_coroutine())
