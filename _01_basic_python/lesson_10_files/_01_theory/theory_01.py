file = open(r'files\example.txt', 'rt', encoding='utf-8')
# print(file)
content = file.read()
file.close()
print(content)

data = ("""Если б мишки были пчелами,
То они бы нипочем
Никогда и не подумали
Так высоко строить дом;

И тогда (конечно, если бы
Пчелы - это были мишки!)
Нам бы, мишкам, было незачем
Лазить на такие вышки!
""")

file = open(r'files\example_write.txt', 'wt', encoding='utf-8')
file.write(data)
file.close()
