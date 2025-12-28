file_lines = []

with open(r'files\example.txt', 'r', encoding='utf-8') as file:
    for line in file:
        file_lines.append(line.rstrip())
        print(line.rstrip())

print(file_lines)

with open(r'files\example_write_01.txt', 'r', encoding='utf-8') as file:
    file_data = file.readlines()

print(file_data)
print(''.join(file_data))
