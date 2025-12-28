# fruits_list = ['apple', 'banana', 'cherry']
# fruits_list_new = fruits_list
# print(fruits_list)
# print(fruits_list_new)
#
# fruits_list_new.append('orange')
# print(fruits_list_new)
# print(fruits_list)
#
# print(fruits_list == fruits_list_new)
# print(fruits_list is fruits_list_new)

fruits_list = ['apple', 'banana', 'cherry']
fruits_list_new = fruits_list[:]
print(fruits_list == fruits_list_new)
print(fruits_list is fruits_list_new)


fruits_list_new1 = list(fruits_list)
print(fruits_list == fruits_list_new1)
print(fruits_list is fruits_list_new1)
