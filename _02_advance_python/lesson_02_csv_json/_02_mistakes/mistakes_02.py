"""
Тип ошибки 2: Символы кириллицы сохраняются в виде escape-последовательностей

Ошибка возникает, когда мы пытаемся записать в JSON-файл словарь,
содержащий кириллицу или другие не-ASCII символы.
"""

import json

data = {
    "Имя": "Андрей",
    "Возраст": 30,
    "Умения": [
        "Python",
        "Data Analysis"
    ]
}
print(json.dumps(data, indent=4))

"""
указываем параметр ensure_ascii=False
"""

print(json.dumps(data, indent=4, ensure_ascii=False))

