class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Публичный атрибут
        self._account_number = "12345"  # Защищённый атрибут
        self.__balance = balance  # Приватный атрибут

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if new_balance > 0:
            self.__balance = new_balance
            print('Баланс успешно изменен!')
        else:
            print('Баланс должен быть положительным!')

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance


if __name__ == '__main__':
    alice_account = BancAccount('Alice', 10000)
    print(alice_account.owner)
    print(alice_account.get_account_number())
    print(alice_account.get_balance())
    alice_account.set_balance(15000)
    print(alice_account.deposit(5000))

    """
    Технически возможно но не надо так делать.
    """
    # print(alice_account._account_number)
    # print(alice_account.__balance)
    # alice_account.owner = 'John'
    # alice_account._account_number = '57689'
    # print(alice_account.owner)
    # print(alice_account._account_number)
