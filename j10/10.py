s = set([1, 2, 3, 1, 2, 3, 4, 4, 4, 5])
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

# print(s1 - s2)
# print(s2 - s1)

# print(s1 | s2)
# print(s1 & s2)

# print(s1 ^ s2)

print(s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1.intersection(s2))
print(s1.union(s2))

s1.intersection_update(s2)