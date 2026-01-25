import re

text = 'Пользователь написал: "Привет" и ушел'
pattern = re.compile(r'"......"')
matches = re.findall(pattern, text)
print(matches)

text = 'Пользователь написал: "Привет" и ушел. А потом добавил "Пока!", ""'
pattern = re.compile(r'"(.*?)"')
matches = re.findall(pattern, text)
print(matches)



