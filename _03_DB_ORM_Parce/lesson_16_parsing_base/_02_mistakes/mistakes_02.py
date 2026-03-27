"""
Тип ошибки 2: Неправильная обработка кодировки

Проблема:
Сайты могут возвращать текст в разных кодировках (например, Windows-1251 вместо UTF-8).
Это приводит к тому, что вместо исходного текста отображаются нечитаемые символы.

Пример ошибки:
"""

import requests
from bs4 import BeautifulSoup

# response = requests.get("https://site.com")
# soup = BeautifulSoup(response.text, "lxml")
# print(soup.find("div"))

"""
Решение:
Принудительно указывать кодировку:
"""
response = requests.get("https://site.com")
response.encoding = "utf-8"  # Или "windows-1251" для более старых сайтов
soup = BeautifulSoup(response.text, "lxml")
print(soup)
