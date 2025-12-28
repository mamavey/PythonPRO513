try:
    # код, который может вызвать ошибку
    number = int(input('Введите целое число: '))
except ValueError:
    print("Это не целое число!")
else:
    print(f'Вы ввели число {number}')


