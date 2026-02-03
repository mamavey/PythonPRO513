"""
Уровень 3. Продвинутый

Задача: реализовать асинхронную функцию monitor_file_uploads(),
которая запускает загрузку нескольких файлов с разными задержками.
Функция должна каждые 2 секунды выводить список файлов,
которые уже загружены, пока не завершится загрузка всех файлов.
"""

import asyncio
from datetime import datetime


async def upload(file_name, delay):
    print(f'Начата загрузка файла {file_name} это займет {delay} секунд.')
    await asyncio.sleep(delay)
    print(f'Файл {file_name} успешно загружен.')
    return file_name


async def monitor_file_uploads(files):
    print(datetime.now())
    tasks = []
    for filename, delay in files:
        print(filename, delay)
        tasks.append(asyncio.create_task(upload(filename, delay)))

    while any(not task.done() for task in tasks):
        # while крутится до тех пор, пока все значения > not task.done() < не будут равны False (not * True = False)
        completed = []
        for task in tasks:
            if task.done():  # проверка выполнения задачи
                completed.append(task.result())  # получение промежуточных результатов
        print(f'Загружено файлов: {len(completed)} ({', '.join(completed)}) прогресс {len(completed) / 3:.2%}')
        await asyncio.sleep(2)

    results = await asyncio.gather(*tasks, return_exceptions=True)
    print(f'Все файлы успешно загружены: ({', '.join(results)})')


if __name__ == '__main__':
    all_files = [("file1.txt", 6), ("file2.txt", 4), ("file3.txt", 8)]
    asyncio.run(monitor_file_uploads(all_files))
