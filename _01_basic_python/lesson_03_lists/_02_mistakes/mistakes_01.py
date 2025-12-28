"""
Тип ошибки 1: Индекс вне диапазона — IndexError: list index out of range
Попытка доступа к элементу списка по индексу, который выходит за пределы списка.
Пример ошибки:
"""

# my_list = [10, 20, 30]
# print(my_list[3])  # IndexError: list index out of range

"""
Решение:
Убедитесь, что индекс, к которому обращаетесь, находится в допустимых границах длины списка.
"""
my_list = [10, 20, 30]
if len(my_list) > 3:
    print(my_list[3])
else:
    print("Индекс вне диапазона")


item_idx = int(input('Введите индекс элемента для отображения: '))
if item_idx > len(my_list) - 1:
    print(f'Индекс выходит за пределы списка')
elif item_idx < -len(my_list):
    print(f'Индекс выходит за пределы списка')
else:
    print(my_list[item_idx])
