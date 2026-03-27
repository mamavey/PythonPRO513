import requests
from bs4 import BeautifulSoup

# Прописываем ссылку на ресурс, который будем парсить
url = 'https://habr.com/ru/articles/'
url_page = "https://habr.com/ru/articles/965432/"
response = requests.get(url=url_page)
html = response.text
print(html)

# 'html.parser' — стандартный парсер для обработки HTML-документов
soup = BeautifulSoup(html, 'html.parser')
# print(soup)


# Находит первый тег с заголовками первого уровня <h1>
title = soup.find('h1')
# print(title)

# Все теги параграфов <p>
all_paragraphs = soup.find_all('p')
# print(all_paragraphs)


# Находит элемент div с классом "tm-article-body" / "article-formatted-body"
article_content = soup.find('div', class_="article-formatted-body")
print(article_content)

# Находит ссылку с указанным href (hyperreference, значением гиперссылки)
# https://habr.com/ru/users/alan_dani/
# author_link = soup.find('a', {'href': 'https://habr.com/ru/users/alan_dani/'})
# print(author_link)
