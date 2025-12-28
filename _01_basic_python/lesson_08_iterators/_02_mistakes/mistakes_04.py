"""
Тип ошибки 4: Неверный объект передан в iter() — TypeError

Функция iter() принимает только итерируемые объекты.
Если передать объект, который не поддерживает итерацию, Python выбросит TypeError.

Пример ошибки:
"""
#
# number = 123  # Число, а не коллекция
# iterator = iter(number)  # Ошибка: TypeError


"""
Убедитесь, что мы используем итерируемый объект, такой как список, строка, множество или кортеж.
"""


def exhaust_iterator(iterator):
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break  # Выходим из цикла, когда элементы заканчиваются


numbers = [1, 2, 3]  # Список — итерируемый объект
nums_iterator = iter(numbers)  # Работает
exhaust_iterator(nums_iterator)

my_dict = {'k1': 'v2', 'k2': 'v2'}
dict_iterator = iter(my_dict.items())
exhaust_iterator(dict_iterator)
