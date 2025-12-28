user_num = input('Введите число: ')
user_num_float = float(user_num)

if user_num_float > 0:
    print(f'Число: {user_num_float} положительное.')
    print('Программа идет дальше')
    if user_num_float > 10:
        print(f'{user_num_float} больше 10')
elif user_num_float == 0:
    print(f'Число: {user_num_float} равно 0')
else:
    print(f'Число: {user_num_float} отрицательное.')
