from os import path

with open(r'files\example_write_02.txt', 'w', encoding='utf-8') as file:
    file.write("Привет мир!\n")
    file.write("Еще строка.\n")

line_list = ['Если б мишки были пчелами,',
             'То они бы нипочем',
             'Никогда и не подумали',
             'Так высоко строить дом;',
             '',
             'И тогда (конечно, если бы',
             'Пчелы - это были мишки!)',
             'Нам бы, мишкам, было незачем',
             'Лазить на такие вышки!']

with open(r'files\example_write_03.txt', 'w', encoding='utf-8') as file:
    for line in line_list:
        file.write(f'{line}\n')

print(path.abspath(r'files\example_write_03.txt'))
