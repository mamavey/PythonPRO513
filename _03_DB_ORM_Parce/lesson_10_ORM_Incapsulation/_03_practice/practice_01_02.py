"""
Задача 1:
Улучшение класса ORM: замена атрибутов на приватные и добавление геттеров
Ситуация:
Ваши коллеги разработали модель ORM, однако не добавили инкапсуляцию,
что делает текущую версию программы уязвимой.
Вы получили код:

class User:
    def __init__(self, id, name, email):
        self.id = id  # Публичный атрибут
        self.name = name  # Публичный атрибут
        self.email = email  # Публичный атрибут

    def save(self):
        # Логика сохранения в базу данных
        print(f"Сохранение пользователя: {self.name}, email: {self.email}")


# Использование
user = User(1, "Иван Иванов", "ivan@example.com")
user.name = ""  # Некорректное значение
user.email = "invalid-email"  # Некорректный email
user.save()  # Сохранение некорректных данных

Задача 1:
Доработайте класс модели в ORM, чтобы все атрибуты были приватными (_ или __).
Добавьте геттеры для получения доступа к данным.
Используйте свойства (@property).

Задача 2: Улучшение класса ORM: добавление сеттеров

Ситуация:
Теперь вам необходимо добавить сеттер для проверки email.
Сеттер проверяет наличие символа @ в строке.
Если символ не обнаружен, сеттер возвращает сообщение об ошибке.

Задача:
Добавить сеттер для проверки email в модуль из задачи 1.
"""
import re


class User:
    users = []

    def __init__(self, user_id, name, email):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        User.add_user(self)

    @classmethod
    def add_user(cls, user_obj):
        cls.users.append(user_obj)

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @name.setter
    def name(self, new_name):
        if len(new_name) <= 3:
            raise ValueError('Имя не может быть короче 3х букв')
        if not new_name.replace(" ", "").replace('-', '').isalpha():
            raise ValueError('Введены недопустимые символы')
        old_name = self.__name
        self.__name = new_name
        User.__report_changes(old_value=old_name, new_value=new_name)

    @email.setter
    def email(self, new_email):
        pattern = re.compile(r'[\w.-]+@[\w.-]+\.[\w.-]+')
        if not bool(pattern.match(new_email)):
            raise ValueError('Некорректный email')
        old_email = self.__email
        self.__email = new_email
        User.__report_changes(old_value=old_email, new_value=new_email)

    @staticmethod
    def __report_changes(old_value, new_value):
        print(f'Данные изменены: {old_value} >> {new_value}')

    def save(self):
        # Логика сохранения в базу данных
        print(f"Сохранение пользователя: {self.name}, email: {self.email}")


if __name__ == '__main__':
    # Использование
    user = User(1, "Иван Иванов", "ivan@example.com")
    user.save()  # Сохранение корректных данных
    print()

    user.name = "Петр Петров"  # Корректное значение
    user.email = "petr@example.com"  # Корректный email
    user.save()  # Сохранение корректных данных

    # user.name = ""  # Ошибка: Имя не может быть пустым
    # user.email = "invalid-email"  # Ошибка: Некорректный email
