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

data = [
    {'balance': 10000},
    {'transaction_type': 'доход', 'amount': 15000, 'category': 'аванс'},
    {'transaction_type': 'расход', 'amount': 5000, 'category': 'жкх'}
]

print(data[0]['balance'])
for d in data[1:]:
    print(d['transaction_type'], d['amount'], d['category'])

