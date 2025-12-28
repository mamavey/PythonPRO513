"""
Тип ошибки 4: Цикл по изменяемому словарю
RuntimeError: dictionary changed size during iteration
Ошибка:
Изменение словаря во время его перебора может привести к ошибке.
Пример ошибки:
"""

# my_dict = {"a": 1, "b": 2, "c": 3}
# for key in my_dict:
#     my_dict.pop(key)  # Ошибка: словарь изменён во время итерации


"""
Создайте копию ключей словаря для безопасного удаления элементов.
"""

my_dict = {"a": 1, "b": 2, "c": 3}
for key in list(my_dict.keys()):
    my_dict.pop(key)
print(my_dict)  # Пустой словарь
