# методы работы с множествами
my_set = {1, 2, 3}

# добавление
my_set.add(4)
print(my_set)

# удаление

num = 2
if num in my_set:
    my_set.remove(num)
    print(f'Элемент {num} удален')
else:
    print(f'Элемент {num} не найден')
print(my_set)

my_set.discard(5)
my_set.discard(1)
print(my_set)

my_set.clear()
print(my_set)
print()

# копирование множеств
my_set_01 = {1, 2, 3}
my_set_02 = my_set_01.copy()
print(my_set_02 is my_set_01)

# длина множества
print(len(my_set_01))
print()

# проверка вхождения
print(2 in my_set_01)
print(5 in my_set_01)
print()


my_str_set = {'item_01', 'item_02', 'item_03', 'item_04', 'item_02'}
random_item = my_str_set.pop()
print(random_item)

