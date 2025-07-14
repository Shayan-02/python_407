# a = "hello"
# print(a[::-1])

lst = [1, 2, 3, 4, 5]
lst2 = []
# print(lst[::-1])
# lst.reverse()
# print(lst)

# for i in range(len(lst)):
#     lst2.append(lst.pop())

for i in range(len(lst) - 1, -1, -1):
    lst2.append(lst[i])

print(lst2)