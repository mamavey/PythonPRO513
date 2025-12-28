"""
Задача 1: Учет сотрудников с наследованием и инкапсуляцией

Ситуация: мы ведем базу данных сотрудников компании.
У каждого сотрудника есть имя, фамилия и базовая зарплата.
Помимо этого, у менеджеров есть бонусы, а у стажеров — сниженная ставка оплаты.
Необходимо использовать наследование и инкапсуляцию, чтобы организовать эту систему.

Задача: создать классы:

Employee (Базовый класс), который содержит:
Приватные поля: first_name, last_name, salary.
Метод для получения полной информации о сотруднике.
Метод для получения зарплаты.

Manager (Класс-наследник от Employee), который:
Имеет дополнительное поле bonus.
Переопределяет метод получения зарплаты, учитывая бонус.

Intern (Класс-наследник от Employee), который:
Имеет дополнительное поле discount_rate (например, 0.5 для 50%).
Переопределяет метод получения зарплаты, учитывая скидку.

Программа должна:
Создавать объекты разных типов сотрудников.
Выводить информацию о них, включая имя, фамилию и итоговую зарплату.
"""


class Employee:
    """Базовый класс сотрудника."""

    def __init__(self, first_name, last_name, salary):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__salary = salary

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if not isinstance(new_salary, (int, float)):
            raise TypeError('Неверный тип данных')
        self.__salary = new_salary

    def get_info(self):
        """Возвращает информацию о сотруднике."""
        return f'{self.first_name} {self.last_name}'


class Manager(Employee):
    """Класс для менеджера, наследуется от Employee."""

    def __init__(self, first_name, last_name, salary, bonus):
        super().__init__(first_name, last_name, salary)
        self.__bonus = bonus

    @property
    def bonus(self):
        return self.__bonus

    @property
    def salary(self):
        """Возвращает зарплату с учетом бонуса, и повышающего коэффициента"""
        return super().salary + self.bonus


class TopManager(Manager):
    """Класс для топ-менеджера, наследуется от Manager."""

    def __init__(self, first_name, last_name, salary, bonus, bonus_rate=1.0):
        super().__init__(first_name, last_name, salary, bonus)
        if bonus_rate < 1.0:
            raise ValueError('Ставка бонуса для топ-менеджера не может быть меньше 1.0')
        self.__bonus_rate = bonus_rate

    @property
    def bonus_rate(self):
        return self.__bonus_rate

    @property
    def salary(self):
        return super().salary * self.bonus_rate


class Intern(Employee):
    """Класс для стажера, наследуется от Employee."""

    def __init__(self, first_name, last_name, salary, discount_rate=0.5):
        super().__init__(first_name, last_name, salary)
        if discount_rate > 0.7:
            raise ValueError('Стажер не может получать более 0.7 от ставки')
        self.__discount_rate = discount_rate

    @property
    def discount_rate(self):
        return self.__discount_rate

    @property
    def salary(self):
        """Возвращает зарплату с учетом понижающего коэффициента."""
        return super().salary * self.discount_rate



