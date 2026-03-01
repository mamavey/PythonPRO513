"""
Тип ошибки 1: Забыли вызвать super().__init__() в дочернем классе
Если вы не вызываете конструктор родительского класса (super().__init__()),
то атрибуты родительского класса не будут инициализированы.
Это может привести к ошибкам при попытке доступа к этим атрибутам.
"""


class Animal:
    def __init__(self, name):
        self.name = name


# class Dog(Animal):
#     def __init__(self, name, breed):
#         self.breed = breed  # Забыли вызвать super().__init__(name)
"""
Всегда вызывайте super().__init__() в конструкторе дочернего класса.
"""


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Вызов конструктора родительского класса
        self.breed = breed


dog = Dog("Бобик", "Дворняжка")
print(dog.name)
