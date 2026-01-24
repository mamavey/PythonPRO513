"""
Задание 2. Базы данных

Ситуация: мы работаем с подключениями к базе данных и должны гарантировать,
что соединение будет закрыто после работы независимо от того, возникли ли ошибки.

Задача — реализовать менеджер контекста для управления соединением с базой данных (имитация).

Шаги реализации:

Создадим класс с методами __enter__ и __exit__.
Метод __enter__ должен возвращать соединение.
Метод __exit__ должен закрывать соединение.
"""


class DBConnection:

    def __init__(self, user, password, server, driver, db_name):
        self.user = user
        self.password = password
        self.server = server
        self.driver = driver
        self.db_name = db_name

    def __enter__(self):
        print(f'Открываем соединение с БД {self.db_name} для пользователя {self.user}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Закрываем соединение с БД {self.db_name} для пользователя {self.user}')
        if exc_type:
            print(f"Произошла ошибка {exc_type.__name__}: {exc_val}")
            return False
        return True


if __name__ == '__main__':
    with DBConnection('Bob', 'qwerty', 'work', 'MS_SQL', 'work_db'):
        print(f'Работаем с БД')
        raise Exception('Что-то пошло не так:(')
