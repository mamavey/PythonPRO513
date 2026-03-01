import re


class User:
    def __init__(self, user_id, name, email):
        self._user_id = user_id
        self._name = name
        self._email = email

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        pattern = re.compile(r'[\w.-]+@[\w.-]+\.[\w.-]+')
        if not bool(pattern.match(value)):
            raise ValueError('Некорректный email')
        old_val = self.email
        self._email = value
        print(f'Изменение почты: {old_val} >> {self.email}')

    def save(self):
        # логика сохранения
        print(f'Сохранение пользователя: {self.name}, email: {self.email}')


if __name__ == '__main__':
    user = User(1, "Иван Иванов", "ivan@example.com")
    user.save()
    user.email = "ivan_new@example.com.ru"
    user.save()
    # user.email = "ivan_new@example"
