"""
Тип ошибки 1: Неправильный выбор парсера

Проблема:

Использование стандартного html.parser для сложных или
HTML-страниц с ошибками в структуре может привести к некорректному разбору структуры.

Пример ошибки:

Этот код может пропустить теги, если они некорректно оформлены в HTML-документе:
"""

from bs4 import BeautifulSoup

broken_html = 'Сломано'
soup = BeautifulSoup(broken_html, "html.parser")
print(soup.find("div"))


"""
Решение:
Использовать более устойчивые парсеры, например lxml:
"""
soup = BeautifulSoup(broken_html, "lxml")
print(soup)