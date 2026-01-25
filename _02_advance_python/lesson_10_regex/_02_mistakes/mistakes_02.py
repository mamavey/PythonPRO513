"""
Возникает, когда спецсимволы, такие как ., *, +, [, ], (, ), {,},не экранированы в случае использования
их как обычных символов.
"""

import re

# text = "Цена: $10A50"
# pattern = re.compile(r'\$\d+.\d+')
# matches = re.findall(pattern, text)
# print(matches)

"""
Решение:
экранируем точку, чтобы она воспринималась как символ, а не как спецсимвол.
"""

text = "Цена: $10A50"
text1 = "Цена: $10.50"
pattern = re.compile(r'\$\d+\.\d{2}')
matches1 = re.findall(pattern, text)
matches2 = re.findall(pattern, text1)
print(matches1)
print(matches2)
