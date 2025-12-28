"""
Тип ошибки 3: Изменение множества во время итерации — RuntimeError: Set changed size during iteration

Ошибка может возникнуть, есть изменить множества во время его перебора.
"""

# my_set = {1, 2, 3}
# for item in my_set:
#     my_set.add(4)
#     print(my_set)


"""
Решение:
Создайте копию множества для безопасной итерации.
"""

my_set = {1, 2, 3}
for item in my_set.copy():  # Итерация по копии
    my_set.add(4)
print(my_set)
