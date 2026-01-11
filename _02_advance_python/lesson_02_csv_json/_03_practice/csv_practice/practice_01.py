"""
Задание 1. Анализ продаж

Ситуация: мы работаем в отделе аналитики и получаем CSV-файл с данными о продажах за месяц.
Каждый ряд содержит следующую информацию: наименование товара, количество проданных единиц и цену за единицу.

Задача — необходимо вычислить общий доход для каждого товара и общий доход за месяц.

Реализуем функцию analyze_sales(file_path), которая:

Читает данные из CSV-файла.
Вычисляет общий доход для каждого товара (количество × цена).
Возвращает итоговый доход за месяц.
"""

import csv
import json


def analyse_sales(filepath):
    sales_list = [{'sales': []}]
    total_revenue = 0
    with open(filepath, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            quantity = int(row['quantity'])
            price = float(row['price'])
            total_revenue += quantity * price
            sales_list[0]['sales'].append(row)
        sales_list.append({'total_revenue': total_revenue})
    return total_revenue, sales_list


def make_json_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as fp:
        json.dump(data, fp, ensure_ascii=False, indent=4)
    return True


if __name__ == '__main__':
    result, info = analyse_sales(r'files\sales.csv')
    print(result)
    print(info)
    make_json_file(r'files\sales.json', info)
