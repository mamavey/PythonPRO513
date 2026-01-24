"""
Тип ошибки 2: Неправильная работа с ресурсами
Возникает, когда разработчик забывает закрыть файл или соединение с базой данных в случае ошибок.
"""

# class OpenToRead:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = None
#
#     def __enter__(self):
#         self.file = open(self.file, 'r', encoding='utf-8')
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         pass  # завершаем метод, не закрыв файл

"""
Решение:

корректно реализовываем логику освобождения ресурсов.
"""


class OpenToRead:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.file, 'r', encoding='utf-8')

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

