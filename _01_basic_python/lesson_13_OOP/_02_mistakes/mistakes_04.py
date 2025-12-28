"""
Тип ошибки 4:
Отсутствие начальных значений для атрибутов объекта — AttributeError: ‘Car’ object has no attribute ‘color’
Ошибка возникает, когда пытаются обратиться к атрибуту, который не был инициализирован.
"""

# class Car:
#     def __init__(self, brand):
#         self.brand = brand  # Только один атрибут инициализирован
#
#
# my_car = Car("Toyota")
# print(my_car.color)  # Ошибка

"""
Решение: Мы пытаемся обратиться к атрибуту color, который не был определён для объекта. 
Задайте все необходимые атрибуты объекта в конструкторе, даже если они имеют значения по умолчанию:
"""

class Car:
    def __init__(self, brand, color="красный"):
        self.brand = brand
        self.color = color


my_car = Car("Toyota")
print(my_car.color)  # Вывод: красный