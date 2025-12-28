name = input("Введите ваше имя: ")

quantity = input('Сколько штук товара вам надо (целое число): ')
quantity_int = int(quantity)

cost_input = input('Введите цену товара: ')
cost_float = float(cost_input)

total_string = f"Привет {name}, количество {quantity_int} шт. товара по цене {cost_float}. Общая сумма {quantity_int * cost_float}"
print(total_string)