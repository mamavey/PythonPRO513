"""
Методы и свойства Tasks:
await task — ожидание завершения таски;
task.done() — проверяет, завершена ли таска;
task.result() — возвращает результат выполнения корутины: если корутина ещё не завершена, вызовет исключение InvalidStateError;
task.cancel() — отменяет выполнение таски: если таска успешно отменена, возвращает True;
task.exception() — возвращает исключение, которое произошло в корутине (если оно было).
"""
from datetime import datetime
from time import sleep
import asyncio


async def my_coroutine():
    print('Start')
    await asyncio.sleep(3)
    print('End')
    return "Done"


async def main():
    print(datetime.now())
    # Создаём задачи
    task = asyncio.create_task(my_coroutine())

    print(f'Task done: {task.done()}')
    await task
    print(f'Task result: {task.result()}')
    print(f'Task done: {task.done()}')
    print(datetime.now())


if __name__ == '__main__':
    asyncio.run(main())


"""
В каких случаях использовать Tasks?

Параллельное выполнение задач — когда нам нужно выполнить несколько асинхронных операций одновременно.

Управление задачами — когда нам нужно отслеживать состояние выполнения задач или отменять их.

Фоновые задачи — когда нам нужно запустить задачу в фоновом режиме, не дожидаясь её завершения.
"""
