import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    url_page = "https://habr.com/ru/articles/803869/"
    response = requests.get(url=url_page, headers=headers, timeout=5)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    title = soup.find('h1', class_='tm-title').text.strip()
    content = soup.find('div', class_='article-formatted-body').text.strip()
    print(f'Заголовок: {title}\n')
    print(f'Текст статьи (начало):\n{content[:300]}')
except requests.exceptions.RequestException as e:
    print(f'Ошибка при запросе: {e}')
except AttributeError:
    print(f'Не удалось найти нужные элементы на странице')
except Exception as e:
    print(f'Что-то не пошло не так: {e}')
