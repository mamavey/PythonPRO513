"""
Тип ошибки 2: Неправильное обращение к атрибуту объекта — NameError: name ‘brand’ is not defined

Ошибка возникает, когда в методе обращаются к атрибуту объекта без использования self.
"""

# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#
#     def drive(self):
#         print(f"{brand} едет!")  # Ошибка: brand не определён
#
#
# my_car = Car("Toyota")
# my_car.drive()


"""
Решение: В методе drive мы пытаемся обратиться к переменной brand, которая не существует в данной области видимости. 
Атрибут brand принадлежит объекту, поэтому нужно использовать self.brand. 
Используйте self для обращения к атрибутам объекта:
"""

class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"{self.brand} едет!")  # Теперь всё работает правильно


my_car = Car("Toyota")
my_car.drive()  # Вывод: Toyota едет!