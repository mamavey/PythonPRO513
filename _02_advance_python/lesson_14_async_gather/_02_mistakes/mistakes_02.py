"""
Тип ошибки 2: Игнорирование исключений в задачах

Возникает, когда одна из задач вызывает исключение.
В этом случае gather завершается с ошибкой, если не использовать параметр return_exceptions=True.
"""
import asyncio

# async def faulty_task():
#     raise ValueError("Ошибка в задаче")
#
#
# async def main():
#     await asyncio.gather(faulty_task(), asyncio.sleep(1))
#
#
# asyncio.run(main())

"""
Решение:

обрабатываем исключения через return_exceptions=True.
"""


async def faulty_task():
    raise ValueError("Ошибка в задаче")


async def main():
    await asyncio.gather(faulty_task(), asyncio.sleep(1), return_exceptions=True)


asyncio.run(main())
