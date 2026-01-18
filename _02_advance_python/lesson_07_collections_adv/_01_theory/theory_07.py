from collections import defaultdict

# Примеры использования defaultdict:
# С list - полезно для группировки данных:

dd = defaultdict(list)
dd['a'].append(1)
dd['b'].append(2)
dd['a'].append(3)

print(dd)
print(dict(dd))

# С int - часто используется для подсчёта элементов:
dd2 = defaultdict(int)
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
for fruit in data:
    dd2[fruit] += 1
print(dd2)
print()


# С пользовательской функцией - можем использовать свою функцию для задания значений по умолчанию:
def default_value():
    return 'значение по умолчание'


dd3 = defaultdict(default_value)
print(dd3['missing_key'])
print(dd3['missing_key1'])
print(dd3)
print()

# my_dict = {'cat': 'кот'}
# print(my_dict.setdefault('cat'))
# print(my_dict.setdefault('dog'))
# print(my_dict)
# print(my_dict.setdefault('rat', "крыса"))
# print(my_dict)
# print()

# Группировка данных - использование defaultdict для группировки элементов по ключу:

data = [('a', 1), ('b', 2), ('a', 3), ('b', 4)]
grouped = defaultdict(list)
for key, value in data:
    grouped[key].append(value)
print(grouped)
