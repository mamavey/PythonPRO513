from datetime import datetime
import asyncio


async def fetch_data(task_id, delay):
    print(f'Task: {task_id} >> started')
    await asyncio.sleep(delay)
    print(f'Task: {task_id} >> finished')
    return f'Data from task {task_id}'


async def main():
    data_requests = [
        fetch_data(task_id=1, delay=2),
        fetch_data(task_id=2, delay=1),
        fetch_data(task_id=3, delay=3),
    ]
    task_list = []
    task_results = []

    for request in data_requests:
        task = asyncio.create_task(request)
        task_list.append(task)

    input('Задача подготовлены. Нажмите ввод для старта выполнения задач: ')
    print(datetime.now())

    for task in task_list:
        await task
        task_results.append(task.result())

    print(task_results)
    print(datetime.now())


if __name__ == '__main__':
    asyncio.run(main())
