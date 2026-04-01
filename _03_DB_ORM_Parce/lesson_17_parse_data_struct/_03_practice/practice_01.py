import requests
from bs4 import BeautifulSoup


def parse_currency_rates(currencies):
    url = "https://www.cbr.ru/currency_base/daily/"

    try:
        # 1. Отправляем HTTP-запрос к странице
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        response.encoding = 'utf-8'
        # 2. Создаем объект BeautifulSoup для анализа HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        # 3. Находим таблицу с курсами
        table = soup.find('table', {'class': 'data'})
        # 4. Инициализируем словарь для результатов
        rates = {}
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            if len(cols) >= 5:
                currency_code = cols[1].text.strip()
                if currency_code in currencies:
                    unit = int(cols[2].text.strip())
                    value = float(cols[4].text.strip().replace(',', '.'))
                    rates[currency_code] = {
                        'value': value,
                        'unit': unit
                    }
        return rates
    except requests.exceptions.RequestException as e:
        print(f'Ошибка при запросе: {e}')
        return None
    except Exception as e:
        print(f'Что-то пошло не так: {e}')
        return None

# if __name__ == '__main__':
#     currency_codes = ['USD', 'EUR', "BYN", "CNY"]
#     result = parse_currency_rates(currency_codes)
#     if result:
#         print(f'Актуальные курсы валют:')
#         for currency, data in result.items():
#             print(f'{currency}: {data['value']} руб. за {data['unit']} ед.')
#     else:
#         print('Не удалось получить данные.')
