import asyncio
from datetime import datetime
import random


async def fetch_data(api_id):
    print(f'Запрос к API {api_id} начат.')
    await asyncio.sleep(random.randint(1, 3))
    print(f'Запрос к API {api_id} завершен.')
    return f'Данные API: {api_id}'


async def main():
    print(datetime.now())
    tasks = [fetch_data(i) for i in range(1, 4)]
    results = await asyncio.gather(*tasks)
    print(f'Все запросы выполнены: {results}')
    print(datetime.now())


async def main1():
    print(datetime.now())
    result1 = await fetch_data(1)
    result2 = await fetch_data(2)
    result3 = await fetch_data(3)
    results = [result1, result2, result3]
    print(f'Все запросы выполнены: {results}')
    print(datetime.now())


if __name__ == '__main__':
    asyncio.run(main())
    print()
    asyncio.run(main1())
