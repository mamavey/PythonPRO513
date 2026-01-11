# my_list = list(range(8 + 1))
# # print(my_list)
#
# evens_list = []
# for element in my_list:
#     if element % 2 == 0:
#         evens_list.append(element)
# print(evens_list)

my_list = list(range(8 + 1))
is_even = lambda x: x % 2 == 0
print(is_even(10))

result = filter(is_even, my_list)
print(result)
print(list(result))
