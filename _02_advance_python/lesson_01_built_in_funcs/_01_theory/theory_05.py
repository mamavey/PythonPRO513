nums_list = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd']

print(list(zip(nums_list, letters)))

for num, letter in zip(nums_list, letters):
    print(f'Число: {num}. Буква: {letter}')
