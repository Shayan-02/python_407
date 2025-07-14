matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

i = 0
j = 0
t = i

while i < len(matrix):
    j = 1
    while j < i:
        print(j, end=" ")
        j += 1
    i += 1
    print()