class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Публичный атрибут
        self._account_number = "12345"  # Защищённый атрибут
        self.__balance = balance  # Приватный атрибут

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance > 0:
            self.__balance = new_balance
            print('Баланс успешно изменен!')
        else:
            raise ValueError("Баланс должен быть положительным!")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance


if __name__ == '__main__':
    alice_account = BankAccount('Alice', 10000)
    print(alice_account.owner)
    print(alice_account.account_number)
    print(alice_account.balance)
    alice_account.balance = 15000
    print(alice_account.deposit(5000))

    try:
        alice_account.balance = -1000
    except ValueError as err:
        print(err)
    print(alice_account.balance)
