person1 = {}  # Пустой словарь
person1['name'] = 'Иван'  # Добавляем ключ 'name' со значением 'Иван'
person1['age'] = 30  # Добавляем ключ 'age' со значением 30
print(person1)

person2 = {'name': 'Мария', 'age': 25}
print(person2)

person3 = dict(name='Алексей', age=35)
print(person3)

person4 = dict([('name', 'Петр'), ('age', 40)])
print(person4)

print(person1['name'])
print(person1['age'])

person5 = {'name': "Екатерина", 'age': 27}
person5['age'] = 28
print(person5)