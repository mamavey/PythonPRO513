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
        if self.file:
            self.file.close()


if __name__ == '__main__':
    with FileWriter(r'example_files\example01.txt', encoding='utf-8') as writer:
        writer.write('Hello World!\n')
        writer.write('Привет Мир!\n')
