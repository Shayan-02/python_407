lst = []

for i in range(1, 11):
    if i % 2 == 0:
        lst.append(i)

print(lst)

print("----------------")

lst2 = [i for i in range(1, 11) if i % 2 == 0]
print(lst2)