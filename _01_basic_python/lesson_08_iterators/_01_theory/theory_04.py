text = "Python"
iterator_text = iter(text)
while True:
    try:
        print(next(iterator_text))
    except StopIteration:
        break
print()

# для повторного использования, необходимо создать новый объект-итератор

iterator_text = iter(text)
while True:
    try:
        print(next(iterator_text))
    except StopIteration:
        break
print()

numbers = {10, 20, 30}
iterator_set = iter(numbers)
for number in iterator_set:
    print(number)
