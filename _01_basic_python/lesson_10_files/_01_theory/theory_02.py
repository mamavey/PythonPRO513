with open(r'files\example.txt', 'r', encoding='utf-8') as file:
    content = file.read()

print(content)

with open(r'files\example_write_01.txt', 'w', encoding='utf-8') as file:
    file.write(content)
