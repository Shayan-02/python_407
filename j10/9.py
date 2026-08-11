lst = [1, 2, 3, 1, 2, 3, 4, 4, 4, 5]
# 1, 2, 3, 4, 5

lst2 = []

for i in lst:
    if i not in lst2:
        lst2.append(i)

print(lst2)