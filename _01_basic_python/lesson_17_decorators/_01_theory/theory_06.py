from functools import wraps


# def authorise(func):
#     @wraps(func)
#     def wrapper(user):
#         if user in ['admin', 'superuser']:
#             return func()
#         else:
#             print(f'Доступ запрещен')
#             return False
#
#     return wrapper
#
#
# @authorise  # в вызов функции надо передать уровень доступа пользователя
# def secret():
#     print(f'Секретная информация')
#
#
# if __name__ == '__main__':
#     secret('admin')
#     secret('user')
#     print(secret.__name__)


def authorise(func):
    @wraps(func)
    def wrapper(user):
        if user in ['admin', 'superuser']:
            return func(user)
        else:
            print(f'Доступ запрещен {user}')
            return False

    return wrapper


@authorise  # в вызов функции надо передать уровень доступа пользователя
def secret(name):
    print(f'Секретная информация {name}')


if __name__ == '__main__':
    secret('admin')
    secret('user')
    print(secret.__name__)
