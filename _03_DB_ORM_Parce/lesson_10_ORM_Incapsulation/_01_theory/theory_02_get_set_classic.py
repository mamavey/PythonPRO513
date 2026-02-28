class User:
    def __init__(self, name, age):
        # «защищённый» атрибут (условно приватный).
        # Доступ к нему возможен, но это считается плохой практикой.
        self._name = name
        # «приватный» атрибут.
        # Python изменяет его имя, чтобы затруднить доступ извне (name mangling).
        self.__age = age

    def get_name(self):
        return self._name

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.__age = value


if __name__ == '__main__':
    user = User(name="Иван", age=35)
    print(user.get_name())
    print(user.get_age())
    user.set_age(36)
    print(user.get_age())
    try:
        user.set_age(-1)
    except ValueError as ve:
        print(ve)
