"""
Тип ошибки 3: Перепутаны методы экземпляра и класса
Ошибка возникает, если мы случайно используем self вместо cls или наоборот.
Пример ошибки:
"""

# class Car:
#     wheels = 4
#
#     @classmethod
#     def describe(self):  # Использован self вместо cls
#         print(f"У всех машин {self.wheels} колеса.")
#
#
# car = Car()
# car.describe()
# Car.describe()

"""
Решение:
Добавьте аргумент cls в метод:
"""

# class Car:
#     wheels = 4
#
#     @classmethod
#     def describe(cls):  # Использован self вместо cls
#         print(f"У всех машин {cls.wheels} колеса.")
#
#     @classmethod
#     def repaint_all(cls):
#         pass
#
#
# Car.describe()
