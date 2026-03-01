class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    # Геттер для баланса
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError('Баланс не может быть отрицательным!')
        self._balance = value

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError('Сумма должна быть положительной')

    def withdraw(self, amount):
        if 0 <= amount <= self.balance:
            self._balance -= amount
        else:
            raise ValueError('Недостаточно средств или неверная сумма!')


if __name__ == '__main__':
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(30)
    print(account.balance)
    account.withdraw(150)
