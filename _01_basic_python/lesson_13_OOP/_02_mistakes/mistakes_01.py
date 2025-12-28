"""
Тип ошибки 1: Пропуск self в методе — TypeError: drive() takes 0 positional arguments but 1 was given
Ошибка возникает, когда метод класса не принимает аргумент self, необходимый для работы с объектом.
"""

# class Car:
#     def drive():
#         print("Машина едет!")
#
#
# my_car = Car()
# my_car.drive()


"""
Решение:
В методах класса первый аргумент всегда должен быть self. Он используется для доступа к атрибутам и методам объекта. 
Без него Python не может передать текущий объект в метод. Добавьте аргумент self в метод:
"""


# class Car:
#     def drive(self):  # self = my_car
#         print("Машина едет!")
#
#
# my_car = Car()
# my_car.drive()
