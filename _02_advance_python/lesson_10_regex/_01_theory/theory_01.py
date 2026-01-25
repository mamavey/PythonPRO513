# text = 'Сегодня 25 апреля 2023 года.'
# words = text.split()
# matches = []
#
# for word in words:
#     if word.isdigit():
#         matches.append(word)
# print(matches)

import re

text = 'Сегодня 25 апреля 2023 года.'
pattern = r'\d+'
matches = re.findall(pattern, text)
print(matches)

text = 'Сегодня 25 апреля 2023 года.'
pattern = re.compile(r'\d+')
matches = re.findall(pattern, text)
print(matches)
