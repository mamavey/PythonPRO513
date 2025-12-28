my_tuple = (1, 2, 3, 4, 5, 6, 7, 3, 3)

second_item = my_tuple[1]
print(second_item)
sub_tuple = my_tuple[2:5]
print(sub_tuple)

new_tuple = my_tuple + (10, 11)
print(new_tuple)

repeated_tuple = my_tuple * 2
print(repeated_tuple)

item = 5
has_item = item in my_tuple
print(has_item)

length = len(my_tuple)
print(length)

count = my_tuple.count(3)
print(count)

item_index = my_tuple.index(3)
print(item_index)