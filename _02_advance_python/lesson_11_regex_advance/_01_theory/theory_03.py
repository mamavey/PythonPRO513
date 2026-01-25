import re

text = "Контактный номер: 81234567890, 71234567890"
pattern = re.compile(r'8\d{10}')
matches = re.findall(pattern, text)
print(matches)

text = "Контактные номера: +7 (123) 456-78-90, 81234567890, 8-123-456-78-90, 8----------()---"
pattern = re.compile(r'\+?\d[\d\s\-()]{10,16}')
matches = re.findall(pattern, text)
print(matches)

print('Введите номер телефона в формате:\n+***(**)******* для РБ\n+*(***)******* для РФ')
phone_number = "Мой номер телефона +375(29)1234567 или +7(922)1234567"

pattern = re.compile(r'\+\d{1,3}\(\d{1,3}\)\d{7}')
print(re.findall(pattern, phone_number))
