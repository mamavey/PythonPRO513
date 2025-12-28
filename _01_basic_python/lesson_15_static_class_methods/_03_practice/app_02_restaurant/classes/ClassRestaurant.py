"""
Задача 2: Управление заказами ресторана

Ситуация: мы создаем систему управления заказами в ресторане.
Каждый заказ связан с определённым номером стола.
В ресторане есть ограниченное количество столов, и если стол занят, то новый заказ для него не принимается.

Задача: создайте программу, которая позволяет:

1) Добавлять заказы на определённый стол.
2) Проверять, свободен ли стол.
3) Узнавать общее количество заказов.
4) Отображать все заказы для каждого стола.
"""


class RestaurantOrder:
    total_orders = 0
    tables = {}

    def __init__(self, table_number, order_details):
        self.table_number = table_number
        self.order_details = order_details
        RestaurantOrder.total_orders += 1
        RestaurantOrder.tables.setdefault(table_number, []).append(order_details)
        #                 {}           {1: []} >> []        [].append(order_details)

    @staticmethod
    def is_table_available(table_number):
        return len(RestaurantOrder.tables.get(table_number, [])) == 0

    @classmethod
    def get_total_orders(cls):
        return f'Всего заказов: {cls.total_orders}'

    def add_order(self, order_details):
        RestaurantOrder.tables.setdefault(self.table_number, []).append(order_details)
        RestaurantOrder.total_orders += 1
