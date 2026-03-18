from functools import wraps


def validate_email(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if hasattr(self, 'email'):
            if '@' not in self.email:
                raise ValueError(f'Некорректный email >> {self.email}')
        return func(self, *args, **kwargs)

    return wrapper


class User:
    def __init__(self, email):
        self.email = email

    @validate_email
    def save(self):
        print(f'Пользователь с {self.email} сохранен')


if __name__ == '__main__':
    user = User('alice@example.com')
    user.save()

    invalid_user = User('invalid_email')
    invalid_user.save()
