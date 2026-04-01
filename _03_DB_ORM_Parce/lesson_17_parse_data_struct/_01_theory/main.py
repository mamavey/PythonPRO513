from theory_01_parser import parse_currency_rates
from theory_02_database import init_db, save_rates_to_db

if __name__ == '__main__':
    currency_codes = ['USD', 'EUR', "BYN", "CNY"]
    currencies = [
        ('USD', 'Доллар США'),
        ('EUR', 'Евро'),
        ('BYN', 'Белорусский рубль'),
        ('CNY', 'Китайский юань'),
    ]
    init_db('currencies', currencies)
    rates = parse_currency_rates(currency_codes)
    if save_rates_to_db('currencies', rates):
        print('Данные успешно сохранены в БД')
    else:
        print(f'Ошибки при сохранении данных')
