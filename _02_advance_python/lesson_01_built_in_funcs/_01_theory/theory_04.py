from functools import reduce

nums_list = [2, 5, 3, 5]
multiply = lambda a, b: a * b

print(reduce(multiply, nums_list))
result = (((2 * 5) * 3) * 5)
        #     10   * 3
        #            30 * 5
print(result)

print(reduce(multiply, nums_list, 10))
result = ((((10 * 2) * 5) * 3) * 5)
print(result)


