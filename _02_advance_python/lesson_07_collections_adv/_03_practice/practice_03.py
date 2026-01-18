"""
Задание 2. Подсчёт продуктов, группировка по категориям

Ситуация: мы работаем над приложением для продуктового магазина.
У нас есть список покупок, где каждый элемент представляет собой кортеж (категория, продукт).
Нам нужно сгруппировать продукты по категориям, чтобы упростить подсчёт.

Задача — реализовать функцию group_products_by_category(items),
которая принимает список кортежей (категория, продукт) и возвращает словарь,
где ключи — категории, а значения — списки продуктов.
Использовать defaultdict для упрощения группировки.

Шаги реализации:
- Создаём defaultdict, где значения — это списки.
- Пройдёмся по каждому элементу списка покупок.
- Добавим продукт в соответствующую категорию.
- Вернём итоговый словарь.
"""

from collections import defaultdict


def group_products_by_category(items: list[tuple[str, str]]) -> defaultdict[str, list[str]]:
    # Создаём defaultdict с типом list для автоматической инициализации
    grouped = defaultdict(list)

    for category, product in items:
        grouped[category].append(product)

    return grouped

def group_products_by_category1(items: list[tuple[str, str]]) -> dict[str, list[str]]:
    products_dict = {}

    for category, product in items:
        if category not in products_dict:
            products_dict[category] = []
            products_dict[category].append(product)
        else:
            products_dict[category].append(product)

    return products_dict


if __name__ == '__main__':
    product_items = [
        ('Фрукты', 'Яблоко'),
        ('Овощи', 'Морковь'),
        ("Фрукты", "Банан"),
        ("Молочные продукты", "Молоко"),
        ("Фрукты", "Апельсин"),
        ("Овощи", "Картофель")
    ]
    result = group_products_by_category(product_items)
    print(result)
    print(dict(result))
    result = group_products_by_category1(product_items)
    print(result)
