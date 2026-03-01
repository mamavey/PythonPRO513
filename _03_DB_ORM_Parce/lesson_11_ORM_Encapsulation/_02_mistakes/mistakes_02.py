"""
Тип ошибки 2: Отсутствие проверок в сеттерах

Сеттеры используются для контроля изменения данных.
Если не добавить проверки, данные могут быть изменены на некорректные значения.
Пример ошибки:
"""


class User:
    def __init__(self, email):
        self._email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value  # Нет проверки на корректность email


user = User("ivan@example.com")
user.email = "invalid-email"  # Некорректный email

"""
Решение:
Добавить проверку данных в сеттере:
"""


class User:
    def __init__(self, email):
        self._email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Некорректный email")
        self._email = value


user = User("ivan@example.com")
user.email = "invalid-email"  # Некорректный email
