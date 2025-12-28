import json

data = [
    {'ключ': 'значение'},
    {'key': 'value'}
]

with open('example.json', 'w', encoding='utf-8') as fp:
    json.dump(data, fp, ensure_ascii=False, indent=4)

with open('example.json', 'r', encoding='utf-8') as fp:
    python_data = json.load(fp)

print(python_data)

# data.extend(python_data)
#
# with open('example.json', 'w', encoding='utf-8') as fp:
#     json.dump(data, fp, ensure_ascii=False, indent=4)

