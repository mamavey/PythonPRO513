# методы заполнения списка

fruits_list = []
fruits_list.append('apple')
fruits_list.append('banana')
fruits_list.append('cherry')
print(fruits_list)

other_fruits_list = ['elderberry', 'pineapple']
fruits_list.extend(other_fruits_list)
print(fruits_list)

other_fruits_01 = ['strawberry', 'plum']
all_fruits_list = fruits_list + other_fruits_01
print(all_fruits_list)

all_fruits_list.insert(2, 'orange')
print(all_fruits_list)
# ['apple', 'banana', 'orange', 'cherry', 'elderberry', 'pineapple', 'strawberry', 'plum']
#     0         1         2         3          4             5             6          7

removed_fruit = 'cherry'
if removed_fruit in all_fruits_list:
    all_fruits_list.remove(removed_fruit)
    print(f'Элемент {removed_fruit} удален')
else:
    print(f'Элемента {removed_fruit} нет в списке')
print(all_fruits_list)

if all_fruits_list:  # если список не пустой
    popped_fruit = all_fruits_list.pop()
    print(f"Удалено {popped_fruit}, в списке осталось: {all_fruits_list}")
else:
    print('Список пуст')

# pop_idx = int(input('Введите индекс элемента для удаления: '))
# if pop_idx > len(all_fruits_list) - 1:
#     print(f'Индекс {pop_idx} выходит за пределы списка')
# elif pop_idx < -len(all_fruits_list):
#     print(f'Индекс {pop_idx} выходит за пределы списка')
# else:
#     popped_fruit1 = all_fruits_list.pop(pop_idx)
#     print(popped_fruit1)
# print(all_fruits_list)

# ['apple', 'banana', 'cherry', 'elderberry', 'pineapple', 'strawberry']
#     0         1         2           3            4            5
#    -6        -5        -4          -3           -2           -1

all_fruits_list = ['apple', 'banana', 'elderberry', 'pineapple', 'strawberry']
all_fruits_list[2] = 'blueberry'
print(all_fruits_list)

# [A-Za-zА-Яа-я]
all_fruits_list.sort()
print(all_fruits_list)
all_fruits_list.sort(reverse=True)
print(all_fruits_list)

nums_list = [3, 4, 1, 8, 9, 5]
nums_list.reverse()
print(nums_list)

sorted_nums_list = sorted(nums_list)
print(sorted_nums_list)
sorted_nums_list_desc = sorted(nums_list, reverse=True)
print(sorted_nums_list_desc)
print(n)

