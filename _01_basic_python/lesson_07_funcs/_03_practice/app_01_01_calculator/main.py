from math_operations import calculator

if __name__ == '__main__':
    while True:
        print('\nПростой калькулятор:')
        try:
            a = float(input('Введите первое число: '))
            b = float(input('Введите второе число: '))
            operation = input('Введите операцию (add, subtract, multiply, divide): ').strip().lower()
            result = calculator(a, b, operation)
            print(f'Результат: {result}')

        except ValueError:
            print('Ошибка введите корректные числа')
        except ZeroDivisionError as zde:
            print(zde)

        user_continue = input('Продолжить? (yes/y/да): ').strip().lower()
        if user_continue not in ['yes', 'y', 'lf', 'да']:
            break
