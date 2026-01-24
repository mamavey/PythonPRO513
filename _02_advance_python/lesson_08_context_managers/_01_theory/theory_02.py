"""
Менеджеры контекста могут обрабатывать исключения, возникающие в теле блока with.

Для этого метод __exit__ принимает три аргумента:
- exc_type — тип исключения (если оно возникло);
- exc_value — само исключение;
- traceback — объект трассировки, который можно использовать для диагностики ошибки.

Если метод __exit__ возвращает True, то исключение не будет выброшено,
иначе оно было бы передано дальше в код.

Например, если мы не хотим, чтобы ошибка прерывала выполнение программы,
можем вернуть True из метода __exit__:
"""


class FileWriter:

    def __init__(self, file_path, encoding=None):
        self.file_path = file_path
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        self.file = open(self.file_path, 'w', encoding=self.encoding)
        return self

    def write(self, data):
        self.file.write(data)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f'Ошибка: {exc_val}')
        self.file.close()
        return True


if __name__ == '__main__':
    # with FileWriter(r'example_files\example02.txt', encoding='utf-8') as writer:
    #     writer.write('Hello World!\n')
    #     writer.write('Привет Мир!\n')
    #     raise Exception('Ошибка при записи')

    strings_list = ['Hello World!\n', 'Привет Мир!\n', 'Привет Гвидо', 'Hello World!\n']
    with FileWriter(r'example_files\example02.txt', encoding='utf-8') as writer:
        for idx, string in enumerate(strings_list):
            if '\n' not in string:
                raise Exception(f'Возникла ошибка в строке {idx + 1}')
            else:
                writer.write(string)
