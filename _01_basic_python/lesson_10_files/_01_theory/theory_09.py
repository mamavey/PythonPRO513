with open(r'files\image.jpg', 'rb') as file:
    data = file.read()

print(f'Прочитано: {len(data)} байт')