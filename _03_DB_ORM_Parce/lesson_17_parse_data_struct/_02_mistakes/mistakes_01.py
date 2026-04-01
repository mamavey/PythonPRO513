"""
Ошибка 1: Неправильная обработка динамических данных
Проблема:
Многие современные сайты загружают данные динамически через JavaScript.
Стандартные HTTP-запросы не получают этот контент.
"""

import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, 'html.parser')
data = soup.find('div', class_='dynamic-content')  # Вернет None

"""
Решение:
Использовать Selenium или инструменты для рендеринга JS:
"""

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
print(soup)
