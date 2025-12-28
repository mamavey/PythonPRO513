"""
Уровень 3: Продвинутый
Задача: разработайте программу для подсчета среднего количества товаров,
поступивших на склад за указанное количество дней.
Программа должна сначала запрашивать у пользователя количество дней для анализа.
Затем для каждого дня должна запрашиваться количество товаров, поступивших на склад.
В конце программа должна вывести среднее количество товаров, поступивших за день.
Если ввод данных некорректен (например, введено отрицательное число дней или товаров, или нечисловое значение),
программа должна сообщать об ошибке и предлагать повторный ввод.
"""

total_goods = 0


class OnlyPositiveException(Exception):
    pass


while True:
    try:
        days_count = int(input('Введите количество дне для анализа: '))
        if days_count < 0:
            raise OnlyPositiveException
        else:
            break
    except OnlyPositiveException:
        print(f'Ошибка ввода: число не может быть отрицательным')
    except ValueError:
        print(f'Ошибка ввода: введите целое число')

for day in range(1, days_count + 1):
    while True:
        try:
            goods_today = int(input(f'Введите количество товаров для {day}-го дня: '))
            if goods_today < 0:
                raise OnlyPositiveException
            else:
                total_goods += goods_today
                break
        except OnlyPositiveException:
            print(f'Ошибка ввода: число не может быть отрицательным')
        except ValueError:
            print(f'Ошибка ввода: введите целое число')

if days_count > 0:
    average_goods = total_goods / days_count
    print(f'Среднее количество товаров, поступивших за день: {average_goods:.2f}')
else:
    print(f'Вы ввели 0 дней анализа, расчет невозможен.')
