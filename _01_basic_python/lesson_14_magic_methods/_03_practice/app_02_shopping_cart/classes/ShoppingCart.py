"""
Задача 2: Виртуальная корзина покупок

Ситуация: мы создаем программу для интернет-магазина.
Нам нужно реализовать класс для корзины покупок, которая позволяет добавлять товары,
удалять их и подсчитывать общую стоимость.
Также пользователи должны видеть, что находится в корзине, в удобочитаемом виде.

Задача: создайте класс Cart, который:

Имеет атрибуты:
- items — список товаров в корзине (по умолчанию пустой).
- каждый товар — это словарь с ключами name (название), price (цена) и quantity (количество).
Использует следующие методы:
- __str__: возвращает строку с перечнем товаров в корзине.
- add_item: добавляет товар в корзину.
- remove_item: удаляет товар из корзины.
- __len__: возвращает количество уникальных товаров в корзине.
- __add__: объединяет две корзины, возвращая новую.
"""


class ShoppingCart:

    def __init__(self):
        self.items = []

    def __str__(self):
        if not self.items:
            return 'Корзина пуста'
        result_string = 'Корзина:\n'
        for item in self.items:
            result_string += f'- {item['name']}: {item['price']} шт. по {item['quantity']} руб.\n'
        return result_string

    def add_item(self, name, price, quantity=1):
        self.items.append({'name': name, 'price': price, 'quantity': quantity})

    def remove_item(self, name):
        # self.items = [item for item in self.items if item['name'] != name]
        items = []
        for item in self.items:
            if item['name'] == name:
                continue
            items.append(item)
        self.items = items

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        if isinstance(other, ShoppingCart):
            new_cart = ShoppingCart()
            new_cart.items = self.items + other.items
            return new_cart
        raise TypeError(
            f"{type(other).__name__} != {type(self).__name__} >> Оба объекта должны принадлежать к классу: {type(self).__name__}")
