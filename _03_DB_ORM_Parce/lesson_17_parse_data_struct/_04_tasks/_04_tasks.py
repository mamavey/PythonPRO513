"""
Перед решением
pip install lxml

Задача1:
Напишите функцию parse_currency_rates(), которая парсит курс выбранной валюты 15 числа каждого месяца,
начиная с апреля 2023 и заканчивая мартом 2025 г., и возвращает эту информацию.
В целях повышения читаемости кода лучше декомпозировать эту функцию на 2.


Задача2:
Доработайте функцию так, чтобы на входе был список интересующих нас валют:
"""

from datetime import timedelta, datetime

import requests
from bs4 import BeautifulSoup


def get_currency_rate(date, curr):
    url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={date.strftime('15/%m/%Y')}"
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Ошибка при получении данных за {date.strftime('15.%m.%Y')}')
        return None

    soup = BeautifulSoup(response.content, 'lxml-xml')
    # XML пример записи валюты.
    # < Valute
    # ID = "R01010" >
    # < NumCode > 036 < / NumCode >
    # < CharCode > AUD < / CharCode >
    # < Nominal > 1 < / Nominal >
    # < Name > Австралийский
    # доллар < / Name >
    # < Value > 59, 8101 < / Value >
    # < VunitRate > 59, 8101 < / VunitRate >
    # < / Valute >
    currency = soup.find('CharCode', string=curr)
    if currency:
        value = currency.find_next_sibling('Value').text
        return float(value.replace(',', '.'))
    else:
        print(f'Валюта не найдена в данных за {date.strftime('%d.%m.%Y')}')
        return None


def get_rates(start_date, end_date, curr_list):
    all_rates = {}
    for curr in curr_list:
        current_date = start_date
        rates = {}
        while current_date <= end_date:
            rate = get_currency_rate(current_date, curr)
            if rate:
                rates[current_date.strftime('15.%m.%Y')] = rate
            current_date += timedelta(days=15)
        all_rates[curr] = rates
    return all_rates


if __name__ == '__main__':
    start = datetime(2024, 10, 15)
    end = datetime(2025, 10, 15)
    rates = ['CNY', 'EUR', 'USD']
    print(get_rates(start, end, rates))
