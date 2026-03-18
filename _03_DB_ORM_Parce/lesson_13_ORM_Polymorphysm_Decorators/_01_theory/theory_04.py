from functools import wraps
import time


def cache_queries(func):
    cache = {}

    @wraps(func)
    def wrapper(self, query):
        if query in cache:
            time.sleep(0.5)  # ТОЛЬКО для наглядности
            print(f'Результат из кэша')
            return cache[query]
        result = func(self, query)
        time.sleep(2)  # ТОЛЬКО для наглядности
        cache[query] = result
        return result

    return wrapper


class Database:
    @cache_queries
    def execute(self, query):
        print(f'Выполнение тяжелого запроса')
        return f'Результат запроса: {query}'


if __name__ == '__main__':
    db = Database()
    print(db.execute('SELECT * FROM users'))  # сохраняет результат запрос в кеше
    print(db.execute('SELECT * FROM users'))  # достает кэшированный результат из кеша