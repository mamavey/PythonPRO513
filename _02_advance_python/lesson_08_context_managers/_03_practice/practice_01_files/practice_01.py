"""
Задание 1. Работа с файлами

Ситуация: мы работаем с текстовыми файлами и часто открываем и закрываем их.
Чтобы избежать ошибок, связанных с забытым закрытием файла, используем менеджеры контекста.

Задача — написать код, который создаёт файл, записывает в него строку,
а затем считывает содержимое и выводит на экран. Использовать конструкцию with для работы с файлом.

Шаги реализации:

1) Создадим файл с использованием менеджера контекста.
2) Запишем текст в файл.
3) Считаем текст из файла и выведем его.
"""


class FileManager:

    def __init__(self, file_path, mode='rt', encoding=None):
        self.file_path = file_path
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, self.mode, encoding=self.encoding)
        return self

    def read(self):
        return self.file.read()

    def write(self, data):
        self.file.write(data)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"Произошла ошибка {exc_type.__name__}: {exc_val}")
            return False
        self.file.close()
        return True


if __name__ == '__main__':
    with FileManager(r'examples\example.txt', 'a', encoding='utf-8') as file:
        file.write('Hello World!\n')

    with FileManager(r'examples\example.txt', encoding='utf-8') as file:
        data = file.read()
        # raise Exception('Произошла ошибка при чтении файла.')

    print(data)
