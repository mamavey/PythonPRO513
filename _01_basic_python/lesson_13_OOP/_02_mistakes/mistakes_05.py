"""
Тип ошибки 5: Перезапись атрибутов объекта через атрибут класса

Ошибка возникает, когда создаётся атрибут объекта с тем же именем, что и атрибут класса,
из-за чего они становятся независимыми.
"""
# class Car:
#     wheels = 4  # Атрибут класса
#
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#
#
# my_car = Car("Toyota", "красный")
# my_car.wheels = 3  # Создаётся новый атрибут объекта
# # my_car.engine_type = 'Бензин'
#
# print(my_car.wheels)  # Вывод: 3
# # print(my_car.engine_type)
# print(Car.wheels)  # Вывод: 4


"""
Решение: Создавая атрибут wheels для объекта, мы не изменяем атрибут класса. 
Они становятся независимыми. Если мы хотим изменить атрибут класса, обращайтесь через имя класса:
"""


class Car:
    wheels = 4  # Атрибут класса

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


Car.wheels = 3
print(Car.wheels)  # Вывод: 3
