def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f'Файл не найден в указанном расположении: {filepath}')
        return None
    except IOError:
        print(f'Ошибка ввода вывода!')
        return None


if __name__ == '__main__':
    my_filepath = input('Введите имя файла: ')
    filepath_read = fr'files\{my_filepath}.txt'
    file_data = read_file(filepath_read)
    if file_data:
        print(file_data)
