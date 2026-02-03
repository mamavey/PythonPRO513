"""
Задание 2. Асинхронная обработка данных

Ситуация: мы разрабатываем приложение для проверки доступности веб-страниц.
Наша цель — асинхронно «скачать» содержимое нескольких страниц и вывести статус их обработки.
Каждая загрузка выполняется с задержкой, чтобы симулировать сетевую операцию.

Задача — реализовать программу для имитации проверки доступности веб-страниц:

- дан список URL-адресов (можно использовать текстовые идентификаторы вместо реальных URL);
- каждая загрузка занимает случайное время от 1 до 5 секунд (asyncio.sleep, библиотека random);
- после завершения загрузки вывести сообщение с информацией о том, какой URL был обработан;
- задачи должны выполняться конкурентно.
"""

import asyncio
import random
from datetime import datetime


async def download_page(url):
    print(f'Начинаю загрузку: {url}')
    download_time = random.uniform(1, 5)
    await asyncio.sleep(download_time)
    print(f'Загрузка завершена. Время загрузки >> {download_time:.2f} секунд.')


async def download_manager(urls):
    # Создаём таски для каждой загрузки
    tasks = []
    for url in urls:
        task = asyncio.create_task(download_page(url))
        tasks.append(task)

    input('Задачи подготовлены. Нажмите ввод для старта выполнения задач: ')
    print(datetime.now())

    for task in tasks:
        await task

    print(datetime.now())


if __name__ == '__main__':
    # Список URL-адресов
    my_urls = [
        "https://example.com/page1",
        "https://example.com/page2",
        "https://example.com/page3",
        "https://example.com/page4",
        "https://example.com/page5",
    ]
    # Запускаем Event Loop
    asyncio.run(download_manager(my_urls))
