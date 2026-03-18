"""
Тип ошибки 1: Отсутствие общего интерфейса для полиморфных методов

Проблема:
Если разные модели ORM используют разные структуры методов,
это усложняет их использование через единый интерфейс.

Пример ошибки:
"""

# class User:
#     def save(self, validate=True):  # Есть параметр validate
#         pass
#
#
# class Product:
#     def save(self):  # Нет параметра validate
#         pass
#
#
# def save_all(models):
#     for model in models:
#         model.save()  # Ошибка, если передать User(validate=False)


"""
Решение:
Унифицировать интерфейсы или использовать **kwargs, 
который позволяет передавать в функцию произвольное количество именованных аргументов.
"""

class User:
    def save(self, **kwargs):
        validate = kwargs.get("validate", True)
        pass

class Product:
    def save(self, **kwargs):
        pass
