matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

first_row = matrix[0]
print(first_row)
element = matrix1[1][1]
print(element)

for a, b, c in matrix1:  # a = 1, b = 2, c = 3/a = 4, b = 5, c = 6....
    print(a, b, c)
