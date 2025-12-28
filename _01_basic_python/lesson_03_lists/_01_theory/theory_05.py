fruits_list = ['apple', 'banana', 'cherry', 'elderberry', 'pineapple', 'strawberry']

for fruit in fruits_list:  # 1) fruit = 'apple' 2) fruit = 'banana' ....
    print(f'Фрукт - {fruit}')
print()


for i in range(len(fruits_list)):
    print(f'Индекс {i} - элемент {fruits_list[i]}')
print()

for idx, item in enumerate(fruits_list):
    print(f'Индекс {idx} - элемент {item}')

