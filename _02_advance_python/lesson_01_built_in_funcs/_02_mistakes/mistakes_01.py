"""
Тип ошибки 1: Функция, работающая с другим типом данных

Ошибка возникает, если с помощью map использовать функцию,
принимающую целочисленные значения к списку,
содержащему значения не только этого типа.
"""

# my_list = [1, 2, "hello", 4, "world"]
# print(list(map(lambda x: len(x), my_list)))

"""
Чтобы избежать этого, можем, например, отфильтровать список и удостовериться, 
что в нём находятся только строки:
"""
my_list = [1, 2, "hello", 4, "world"]
filtered_list = list(filter(lambda x: type(x) is str, my_list))
print(filtered_list)
print(list(map(lambda x: len(x), filtered_list)))
