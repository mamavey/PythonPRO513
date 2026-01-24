"""
Задание 2. Дата доставки

Ситуация: вы разрабатываете бэкенд для сайта интернет магазина.
На текущем этапе необходимо разработать логику рассчитывания даты доставки заказа.
Известно, что любой заказ придет не позже, чем через пять рабочих дней после оформления.

Задача — написать программу, которая вычисляет дату доставки заказа без учета выходных дней.

Шаги реализации:

1) Импортируем модули datetime и timedelta.
2) Создадим объект datetime для текущего времени.
3) Рассчитаем дату, прибавив 5 рабочих дней, исключив выходные.
4) Выведем полученную дату доставки.
"""

from datetime import datetime, timedelta


# Функция для вычисления даты с учётом рабочих дней

def add_weekdays(start_date, num_days):
    current_date = start_date
    while num_days > 0:
        current_date += timedelta(days=1)
        if current_date.weekday() < 5:
            num_days -= 1
    return current_date


if __name__ == '__main__':
    date_now = datetime.now()
    delivery_date = add_weekdays(date_now, 5)
    print(f'Дата доставки: {delivery_date.strftime('%d.%m.%Y >> %H:%M:%S')}')

    date_monday = datetime(2026, 1, 12, 20, 37, 00)
    delivery_date = add_weekdays(date_monday, 5)
    print(f'Дата доставки: {delivery_date.strftime('%d.%m.%Y >> %H:%M:%S')}')