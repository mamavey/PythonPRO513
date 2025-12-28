"""
Тип ошибки 1: Неправильное использование super() в наследовании

Ошибка возникает, если забыть вызвать super().__init__()
при переопределении конструктора в дочернем классе.
Это приведёт к тому, что родительский класс не инициализируется.
"""


class Animal:
    def __init__(self, name):
        self.name = name


# class Dog(Animal):
#     def __init__(self, name, breed):
#         # Ошибка: Не вызван super().__init__(name)
#         self.breed = breed
#
# dog = Dog("Шарик", "Овчарка")
# print(dog.name)  # AttributeError: 'Dog' object has no attribute 'name'


"""
Решение:
Не забывайте вызывать конструктор родительского класса.
"""


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


# class Cat(Animal):
#     def __init__(self, name, breed):
#         Animal.__init__(self, name)
#         self.breed = breed


dog = Dog("Шарик", "Овчарка")
print(dog.name)  # AttributeError: 'Dog' object has no attribute 'name'

cat = Cat('Мурзик', 'Дворянин')
print(cat.name)
