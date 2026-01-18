"""
Тип ошибки 3: Слишком короткие или неточные описания

Возникает, когда docstrings функции слишком кратко описывают её логику/не описывают вовсе.
Это также может приводить к неправильному восприятию поведения функции другими разработчиками.

Пример ошибки:
"""

# def find_discount(price, discount):
#     """Calculate discount"""
#     return price - price * discount


"""
Решение: подробнее расписываем логику функции в docstrings, указываем принимаемые аргументы.
"""


def find_discount(price: float, discount: float) -> float:
    """
    Функция находит значение цены со скидкой

    Параметры:
        price (float): цена
        discount (float): размер скидки от 0 до 1

    Возвращает:
        price_with_discount (float): расчет цены со скидкой

    """
    price_with_discount = price - price * discount
    return price_with_discount


print(find_discount(1000, 0.55))
