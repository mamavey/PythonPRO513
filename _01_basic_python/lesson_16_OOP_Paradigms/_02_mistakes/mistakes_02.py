"""
Тип ошибки 2: Доступ к защищенным или приватным атрибутам

Ошибка возникает только при попытке получить доступ к приватным атрибутам (__private)
за пределами класса, так как Python вызывает AttributeError.
Однако для защищенных атрибутов (_protected) ошибки не будет, но их использование
за пределами класса или его наследников нарушает принцип инкапсуляции и считается плохой практикой.
"""

# class BankAccount:
#     def __init__(self, owner, balance):
#         self._account_number = "12345"  # Защищенный атрибут
#         self.__balance = balance  # Приватный атрибут
#
# account = BankAccount("Алиса", 1000)
# print(account.__balance)


"""
Решение:

Используйте методы (геттеры и сеттеры) для доступа к данным.
"""


class BankAccount:
    def __init__(self, owner, balance):
        self._account_number = "12345"  # Защищенный атрибут
        self.__balance = balance  # Приватный атрибут

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self.__balance
