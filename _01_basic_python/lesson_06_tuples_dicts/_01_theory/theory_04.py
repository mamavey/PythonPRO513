contact_info = {'name': "Мария", 'age': 25, 'email': "maria@gmail.com"}

# Проверка наличия ключа
if 'email' in contact_info:
    print('Email найден!')

# Добавление новой пары ключ-значение
contact_info['phone'] = "123-456-7890"

# Обновление значения
contact_info.update({'age': 26})
# contact_info['age'] = 26

# Получение всех ключей, значений и пар
print(list(contact_info.keys()))
print(list(contact_info.values()))
print(list(contact_info.items()))
