class User:
    def __init__(self, name, age):
        # «защищённый» атрибут (условно приватный).
        # Доступ к нему возможен, но это считается плохой практикой.
        self._name = name
        # «приватный» атрибут.
        # Python изменяет его имя, чтобы затруднить доступ извне (name mangling).
        self.__age = age


if __name__ == '__main__':
    user = User(name="Иван", age=35)
    print(user._name)  # Доступ к защищённому атрибуту (не рекомендуется)
    # print(user.__age)  # Ошибка: AttributeError
    print(user._User__age)  # Доступ к приватному атрибуту (через name mangling)
