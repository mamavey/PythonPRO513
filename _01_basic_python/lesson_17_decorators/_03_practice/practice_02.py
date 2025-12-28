"""
Задача 2: Авторизация доступа к секретным данным

Ситуация: мы разрабатываем систему для управления секретными данными,
доступ к которым должен быть только у пользователей с правами администратора.
Необходимо автоматически проверять права доступа перед выполнением функции.

Задача: создать декоратор authorize_admin, который:

Проверяет, является ли пользователь администратором.
Если пользователь администратор, выполняет функцию.
Если пользователь не администратор, выводит сообщение «Доступ запрещён».
"""

from functools import wraps


def authorise_admin(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.get('role') == 'admin':
            print(f'Пользователь: {user['name']} получил доступ:')
            return func(user, *args, **kwargs)
        else:
            print(f'Доступ запрещен для пользователя {user['name']}')
            return False

    return wrapper


@authorise_admin
def view_secret_data(user):
    print(f'Секретные данне для пользователя {user['name']}')


if __name__ == '__main__':
    admin_user = {'name': 'Alice', 'role': 'admin'}
    regular_user = {'name': 'Bob', 'role': 'user'}
    view_secret_data(admin_user)
    print()

    view_secret_data(regular_user)
