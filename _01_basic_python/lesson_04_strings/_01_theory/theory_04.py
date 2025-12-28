# Разделение строки
text = "Python is fun"
words_list = text.split()
print(words_list)

csv_line = "one,two,three"
items = csv_line.split(',')
print(items)


# Объединение строки
joined = ' '.join(words_list)
print(joined)
csv_joined = ','.join(items)
print(csv_joined)
