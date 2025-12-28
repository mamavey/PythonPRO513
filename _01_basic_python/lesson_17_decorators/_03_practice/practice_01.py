"""
Задача 1: Логирование действий пользователя

Ситуация: мы разрабатываем приложение, которое отслеживает действия пользователей,
такие как вход в систему, обновление профиля или отправка сообщения.
Для каждого действия нужно сохранять лог с именем пользователя и названием выполненной функции.
Лог-файлы позволяют анализировать действия пользователей и выявлять ошибки в работе системы.

Задача: создать декоратор log_action, который:

- Логирует имя пользователя и выполняемое действие.
- Сохраняет эту информацию в текстовый файл actions.log.
- Работает с любыми функциями, которые принимают username как первый аргумент.
"""
from datetime import datetime
from functools import wraps


def log_action(func):
    @wraps(func)
    def wrapper(username, *args, **kwargs):
        if not username:
            with open('actions.log', 'a', encoding='utf-8') as log_file:
                log_file.write(f'{datetime.now()} - Неавторизованный доступ\n')
            print('Вы не авторизованы')
            return False
        with open('actions.log', 'a', encoding='utf-8') as log_file:
            log_file.write(f'{datetime.now()} - Пользователь {username}, действие: {func.__name__}\n')
        return func(username, *args, **kwargs)

    return wrapper


@log_action
def login(username):
    print(f'{username} вошел в систему')
    return username


@log_action
def update_profile(username, profile_data):
    print(f'{username} обновил профиль с данными: {profile_data}')


if __name__ == '__main__':
    user_log = login('Alice')
    update_profile(user_log, {'age': 25, 'city': 'Moscow'})

    update_profile(None, {'age': 33, 'city': 'Minsk'})
