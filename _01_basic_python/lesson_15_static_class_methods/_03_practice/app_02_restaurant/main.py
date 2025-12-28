from classes.ClassRestaurant import RestaurantOrder

if __name__ == '__main__':
    order1 = RestaurantOrder(1, "Салат Цезарь")
    order2 = RestaurantOrder(2, "Пицца Маргарита")
    print(RestaurantOrder.is_table_available(3))  # True, стол 3 свободен
    print(RestaurantOrder.is_table_available(1))  # False, стол 1 занят
    print(RestaurantOrder.get_total_orders())  # Вывод: Всего заказов: 2
    print(RestaurantOrder.tables)
    order1.add_order('Пицца Везувий')
    print(RestaurantOrder.tables)
    print(RestaurantOrder.get_total_orders())
