"""
Задание 1. Мониторинг теплицы

Ситуация: мы разрабатываем систему «умный дом» и в данный момент работаем над другой системой,
контролирующей микроклимат в теплице. Для контроля условий выращивания растений установлены два датчика:

- Датчик температуры измеряет температуру внутри теплицы.
- Датчик влажности измеряет уровень влажности воздуха.

Задачи:
- Реализовать имитацию сбора данных с двух датчиков за заданное время.
Датчики передают измерения с разным интервалом (зависит от настроек и их работы).
- Конкурентно получать данные с двух датчиков,
чтобы не терять время в ожидании завершения работы одного из них.

Используем asyncio.sleep и библиотеку random для имитации задержек.
"""

import asyncio
import random
from datetime import datetime


async def temperature_sensor():
    """Симуляция работы датчика температуры"""
    for _ in range(5):
        gather_time = random.uniform(1, 3)
        await asyncio.sleep(gather_time)
        temperature = random.uniform(10, 35)
        print(f'[Температура] Данные: {temperature:.2f}°C >> t сбора {gather_time:.2f} секунд')


async def humidity_sensor():
    """Симуляция работы датчика влажности"""
    for _ in range(5):
        gather_time = random.uniform(1, 3)
        await asyncio.sleep(gather_time)
        humidity = random.uniform(10, 35)
        print(f'[Влажность] Данные: {humidity:.2f}% >> t сбора {gather_time:.2f} секунд')


async def main():
    print(datetime.now())
    temperature_task = asyncio.create_task(temperature_sensor())
    humidity_task = asyncio.create_task(humidity_sensor())

    # Ожидаем завершения всех задач
    await temperature_task
    await humidity_task
    print(datetime.now())


if __name__ == '__main__':
    asyncio.run(main())

