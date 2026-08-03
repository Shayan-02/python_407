lst = ["ali", "reza", "mohammad", "reza"]

lst.append("amir")
lst.insert(1, "ahmad")

lst.pop()
lst.pop(1)
lst.remove("reza")

print(lst)

lst.clear()
print(lst)

del lst
print(lst)