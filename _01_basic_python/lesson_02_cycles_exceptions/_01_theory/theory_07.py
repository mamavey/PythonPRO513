try:
    # код, который может вызвать ошибку
    user_num = int(input('Введите целое число: '))
    result = 10 / user_num
    # file = open('blabla.txt')
except ZeroDivisionError:
    print(f'На ноль делить нельзя!')
except ValueError:
    print(f'Это не целое число!')
except Exception:
    print('Что-то пошло не так!')
else:
    print(f'10 / {user_num} == {result}')
finally:
    print(f'Программа завершена!')
