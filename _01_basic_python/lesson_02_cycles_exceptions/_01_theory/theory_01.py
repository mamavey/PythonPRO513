# обычный цикл for .... range(num)
for number in range(10):
    print(number)
print()

# print(list(range(10)))

# цикл в котором указана точка отсчета
for number in range(1, 11):
    print(number)
print()

# цикл с шагом
for number in range(0, 11, 2):
    print(number)
print()

# цикл с шагом -1
for number in range(10, -1, -1):
    print(number)
print()

# цикл с прерыванием
for number in range(0, 11):
    if number == 5:
        break
    else:
        print(number)
print()

# цикл с continue
for number in range(1, 11):
    if number == 5 or number == 7:
        continue
    print(number)
print()
