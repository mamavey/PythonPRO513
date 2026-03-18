from functools import wraps


def log_sql(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Выполняется SQL: {func.__name__}')
        print(f'Аргументы: {args[1:]}, {kwargs}')
        result = func(*args, **kwargs)
        print(f'Результат >> {result}')
        return result

    return wrapper


class Database:
    @log_sql
    def execute(self, query):
        # Здесь была бы реальная логика выполнения SQL
        return f'Результат запроса "{query}"'


if __name__ == '__main__':
    db = Database()
    db.execute('SELECT * FROM users;')
