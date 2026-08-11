lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst)

for i in lst:
    for j in i:
        print(j, end="\t")
    print()


print("-"*30)

for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j], end="\t")
    print()