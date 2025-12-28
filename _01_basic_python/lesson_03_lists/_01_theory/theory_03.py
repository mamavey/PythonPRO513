numbers = [10, 20, 30, 40, 50, 60, 70, 80]
#           0   1   2   3   4   5   6  7
my_num_01 = numbers[3]
print(my_num_01)
print(numbers)

my_slice = numbers[1:5]  # с какого, строго до какого
print(my_slice)

my_slice1 = numbers[:4]
print(my_slice1)

my_slice2 = numbers[4:]
print(my_slice2)

my_step_slice = numbers[::2]
print(my_step_slice)

my_step_slice1 = numbers[1:6:2]
print(my_step_slice1)

print(len(numbers))
