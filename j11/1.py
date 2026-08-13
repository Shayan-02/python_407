lst = [-10, -15, -5 ,-25]

max_ = lst[0]
min_ = lst[0]

# print(max(lst))
# print(min(lst))
# print(sum(lst))

for i in range(len(lst)):
    if lst[i] > max_:
        max_ = lst[i]

for i in range(len(lst)):
    if lst[i] < min_:
        min_ = lst[i]

print(max_)
print(min_)