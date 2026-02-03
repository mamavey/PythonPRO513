"""
Задание 2. Сканирование портов
Ситуация: в нашей компании случилась утечка данных, и отдел кибербезопасности предполагает,
что проблема в открытом порте на одном из серверов.
Нам поставили задачу написать утилиту, проверяющую наличие утечек данных.
Для ускорения работы нужно выполнять проверку нескольких портов одновременно.

Задача:
Написать программу, которая будет имитировать проверку списка портов.
Время проверки каждого порта составляет от 1 до 3 секунд (использовать модуль random).
После завершения проверки каждого порта вывести сообщение об успехе или ошибке (например, порт закрыт).
Все проверки должны выполняться параллельно.
"""
import asyncio
import random
from datetime import datetime


async def check_port(port):
    """Симуляция проверки порта."""
    delay = random.uniform(1, 3)
    print(f'Проверка порта {port} начата (займет {delay:.2f} сек.).')
    await asyncio.sleep(delay)
    is_open = random.choice([True, False])
    if is_open:
        print(f'Порт {port} открыт')
    else:
        print(f'Порт {port} закрыт')


async def check_all_ports(ports):
    print(datetime.now())
    print(f'Начинаем сканирование портов...\n')
    # Создаём таски для проверки портов
    tasks = [check_port(port) for port in ports]
    # Ожидаем завершения всех задач
    await asyncio.gather(*tasks, return_exceptions=True)
    print(f'\nСканирование завершено.')
    print(datetime.now())


if __name__ == '__main__':
    all_ports = [22, 80, 443, 8080, 3306]
    asyncio.run(check_all_ports(all_ports))
