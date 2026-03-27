import requests
from bs4 import BeautifulSoup

# Прописываем ссылку на ресурс, который будем парсить
url_page = "https://habr.com/ru/articles/965432/"
response = requests.get(url=url_page)
html = response.text
# print(html)

# 'html.parser' — стандартный парсер для обработки HTML-документов
soup = BeautifulSoup(html, 'html.parser')


# Находит первый тег с заголовками первого уровня <h1>
title = soup.find('h1').text.strip()
# print(title)


# Находит элемент div с классом "tm-article-body" / "article-formatted-body"
article_content = soup.find('div', class_="article-formatted-body").text.strip()
# print(article_content)
print(f'Заголовок: {title}\n\n{article_content[:200]}')

