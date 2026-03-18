"""
Задача 1: Базовый ORM-класс с полиморфным методом save()

Ситуация:
Вы работаете в команде над ORM-системой, которая сохраняет информацию о пользователях системы.
Вы и ваши коллеги обнаружили, что код дублируется при сохранении разных типов данных.
Вы решили применить свойство полиморфизма для решения обнаруженной проблемы.

Задача:
Создайте базовый класс Model, который будет содержать общую логику для всех моделей, метод save().
Класс User наследуется от Model и реализует свою версии метода save().
"""


class Model:
    def save(self):
        print(f'Начало процесса сохранения')


class User(Model):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        super().save()
        print(f'Сохранение пользователя: {self.name}, email {self.email}')


"""
Задача 2: Создание нового метода ORM-класса

Ситуация:
Теперь вам необходимо добавить класс Product для разрабатываемой ORM и проверить работоспособность системы.

Задача:
Создайте класс Product, который наследуется от Model и реализует свою версию метода save().
"""


class Product(Model):
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def save(self):
        super().save()
        print(f'Сохранение товара: {self.title}, цена: {self.price}')


if __name__ == '__main__':
    user = User('Alice', 'alice@mail.ru')
    user.save()
    print()

    product = Product('Smartphone', 50000)
    product.save()
