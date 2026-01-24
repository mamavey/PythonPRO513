import time
from datetime import datetime


class DBConnection:
    def __enter__(self):
        print(f'Открываем соединение с БД')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Закрываем соединение с БД')
        if exc_type:
            print(f'Произошла ошибка: {exc_val}')
            return False
        return True


class FileWriter:
    def __enter__(self):
        self.file = open(r'example_files\log.txt', 'a', encoding='utf-8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
            print(f'Ошибка в файле: {exc_val}')
            return False
        return True


if __name__ == '__main__':
    with DBConnection() as db, FileWriter() as file:
        print(f'{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} >> Подключение к БД\n')
        file.file.write(f'{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} >> Подключение к БД\n')
        time.sleep(2)
        print(f'Продолжаем работать с БД')
        time.sleep(2)
        print(f'{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} >> Отключение от БД\n')
        file.file.write(f'{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} >> Отключение от БД\n')
