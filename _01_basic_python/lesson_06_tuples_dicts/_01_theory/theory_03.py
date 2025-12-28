# person = {'name': "Мария", 'age': 25}

# key = 'surname'
# if key in person:
#     print(person[key])
# else:
#     print(f'Ключ {key} не найден')


# # .get(key) — возвращает значение для указанного ключа,
# # если ключ существует в словаре.
# # Если ключа нет, возвращает None, или заданное значение:
#
# age = person.get('age', 'возраст не указан')
# print(age)
# surname = person.get('surname', 'Фамилия не указана')
# print(surname)
# print(person)
# print()

# surname = person.get('surname')
# if surname:
#     print(surname)
# else:
#     print(f'Введите вашу фамилию')

# # .setdefault(key, value) — возвращает значение для указанного ключа,
# # если ключ существует в словаре.
# # Если ключа нет, возвращает None, или заданное значение при этом создавая новую пару ключ: значение:
# person = {'name': "Мария", 'age': 25}
# name = person.setdefault('name', 'Имя не указано')
# print(name)
# print(person)
# surname = person.setdefault('surname', 'фамилия не указана')
# print(surname)
# print(person)


person = {'name': "Мария", 'age': 25}
# .keys() — возвращает объект, содержащий ключи словаря:
keys = person.keys()
print(keys)
print(type(keys))
keys_list = list(keys)
print(keys_list)
print()

# .values() — возвращает объект, содержащий значения словаря:
values = person.values()
print(values)
print(type(values))
print()

# .items() — возвращает объект с парами (ключ, значение):
items = person.items()
print(items)
print(type(items))
print()

person = {'name': "Мария", 'age': 25}
# .update(other) — обновляет словарь, добавляя пары (ключ, значение) из другого словаря.
# Существующие ключи обновляются, новые ключи добавляются:
person.update({'age': 26, 'city': 'Москва'})
print(person)
print()

# удаление пары ключ значения
name = person.pop('name')
print(name)
