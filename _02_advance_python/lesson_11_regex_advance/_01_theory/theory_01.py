import re

phone_number = "89001234567"
pattern = re.compile(r'\d\d\d\d\d\d\d\d\d\d\d')
print(re.findall(pattern, phone_number))
