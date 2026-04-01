-- Таблица справочника валют
CREATE TABLE IF NOT EXISTS currencies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,        -- Буквенный код (USD, EUR)
    name TEXT NOT NULL               -- Название валюты
);

-- Таблица исторических курсов
CREATE TABLE IF NOT EXISTS exchange_rates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    currency_id INTEGER NOT NULL,    -- Ссылка на валюту
    date TEXT NOT NULL,              -- Дата курса (YYYY-MM-DD)
    value REAL NOT NULL,             -- Значение курса
    FOREIGN KEY (currency_id) REFERENCES currencies(id),
    UNIQUE (currency_id, date)       -- Уникальность пары валюта – дата
);

-- Индексы для ускорения запросов
CREATE INDEX IF NOT EXISTS idx_currency_code ON currencies(code);
CREATE INDEX IF NOT EXISTS idx_rate_date ON exchange_rates(date);
CREATE INDEX IF NOT EXISTS idx_rate_currency ON exchange_rates(currency_id);