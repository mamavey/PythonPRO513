import requests


# Получаем список задач для пользователя с ID 1
def display_tasks(url):
    response = requests.get(url)
    if response.status_code == 200:
        todos = response.json()
        # print(todos[0])
        for task in todos:
            if task['completed']:
                task_status = 'Выполнена'
            else:
                task_status = 'Не выполнена'
            print(f'Задача {task['id']}: {task['title']} >> {task_status}')
    else:
        print(f'Ошибка: {response.status_code}')


# Размещение новой задачи
def post_task(url, task_data):
    response = requests.post(url, json=task_data)
    if response.status_code == 201:
        print(response.json())
    else:
        print(f'Ошибка: {response.status_code}')


if __name__ == '__main__':
    get_url = 'https://jsonplaceholder.typicode.com/users/1/todos'
    display_tasks(url=get_url)
    post_url = 'https://jsonplaceholder.typicode.com/todos'
    new_task = {
        'userId': 1,
        'title': 'Купить молоко',
        'completed': False
    }
    post_task(url=post_url, task_data=new_task)
