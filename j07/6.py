lst = [1, 2, 3, 4, 4, 5, 1, 2, 3, 4, 5, "reza", "ali", "mamad", True, True, False, 6, 6.5, 6, 735, 433]

b = []

for i in lst:
    if i not in b:
        b.append(i)

print(b)