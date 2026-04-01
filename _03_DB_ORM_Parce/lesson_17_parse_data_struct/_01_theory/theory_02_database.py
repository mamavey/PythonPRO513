import sqlite3
from datetime import datetime


def init_db(database_name, currencies: list[tuple[str, str]]):
    conn = sqlite3.connect(fr'databases\{database_name}.db')
    cursor = conn.cursor()
    # Создаем таблицы, если они не существуют
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS currencies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL
        )
        """)

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS exchange_rates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                currency_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                value REAL NOT NULL,
                FOREIGN KEY (currency_id) REFERENCES currencies(id)
            )
            """)

    cursor.executemany(
        "INSERT OR IGNORE INTO currencies (code, name) VALUES (?, ?)", currencies
    )
    conn.commit()
    conn.close()


def save_rates_to_db(database_name, rates):
    if 'error' in rates:
        return False
    conn = sqlite3.connect(fr'databases\{database_name}.db')
    cursor = conn.cursor()
    today = datetime.now().strftime('%Y-%m-%d')
    for currency, data in rates.items():
        # Получаем ID валюты
        cursor.execute(
            'SELECT id FROM currencies WHERE code = ?', (currency,)
        )
        currency_id = cursor.fetchone()[0]

        # Сохраняем курс
        cursor.execute("""
            INSERT INTO exchange_rates
            (currency_id, date, value) VALUES (?, ?, ?)
        """, (currency_id, today, data['value']))
    conn.commit()
    conn.close()
    return True

#
# if __name__ == '__main__':
#     my_currencies = [
#         ('BYN', 'Белорусский рубль'),
#         ('USD', 'Доллар США'),
#         ('EUR', 'Евро')
#     ]
#     init_db('currencies', my_currencies)
