class BankAccount:
    interest_rate = 0.05

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.balance += amount
            print(f'{self.owner} пополнил счет на {amount}. Новый баланс: {self.balance}')
        else:
            print(f'Ошибка неверная сумма! Или неверный тип данных!')

    @staticmethod
    def is_valid_amount(amount):
        if not isinstance(amount, (int, float)):
            return False
        return amount > 0

    @classmethod
    def set_interest_rate(cls, new_rate):
        # cls.interest_rate = new_rate
        # print(f'Процентная ставка изменена на {cls.interest_rate * 100:.2f}%')
        old_rate = cls.interest_rate
        cls.interest_rate = new_rate
        print(f'Процентная ставка изменена: {old_rate * 100:.2f}% >> {cls.interest_rate * 100:.2f}%')


if __name__ == '__main__':
    account_ivan = BankAccount('Иван', 1000)
    # работа с экземпляром
    account_ivan.deposit(-200)
    account_ivan.deposit("200")
    account_ivan.deposit(200)
    print()

    # работа с классом
    BankAccount.set_interest_rate(0.07)
    print(BankAccount.interest_rate)
    print()

    # использование staticmethod вне класса
    print(BankAccount.is_valid_amount(200))
    print(BankAccount.is_valid_amount(-200))

    # ivan_sum = float(input('Введите сумму пополнения: '))
    # if BankAccount.is_valid_amount(ivan_sum):
    #     account_ivan.deposit(ivan_sum)
    # else:
    #     print(f'Отказ из основного кода')
