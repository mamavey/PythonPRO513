# nums_list = [1, 2, 3]
# squares_list = []
# for num in nums_list:
#     squares_list.append(num ** 2)
# print(squares_list)

nums_list = [1, 2, 3]
result = map(lambda x: x ** 2, nums_list)
print(result)
print(list(result))

for value in map(lambda x: x ** 2, nums_list):
    print(value)
print()


def calculate_square(x):
    if type(x) is int:
        return x ** 2
    else:
        return None


nums_list = [1, 2, 3, 'str']
result = map(calculate_square, nums_list)
print(list(result))

upper_lambda = lambda letter: letter.upper()
result = map(upper_lambda, 'привет')
print(''.join(result))
