count = 0

while count < 10:  # if count == 10: >> цикл прерывается и инструкции в теле цикла не выполняются
    print(count)
    # count = count + 1
    count += 1
print()

count = 1

while True:
    if count == 15:
        break
    print(count)
    count += 1
print()

count = 1
while count < 11:
    if count == 5:
        print(f'!!!!{count}!!!!')
        count += 1
        continue
    print(count)
    count += 1
print()
