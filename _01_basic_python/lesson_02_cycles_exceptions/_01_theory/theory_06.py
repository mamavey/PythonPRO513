try:
    file = open('example.txt')
    data = file.read()
except FileNotFoundError:
    print(f'Файл не найден!')
else:
    file.close()
finally:
    print('Файл закрыт')


