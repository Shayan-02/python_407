# a = [] # a = list()

lst = [1, "ali", 3, False, None]
print(len(lst), end="\n=================\n")

# for i in lst:
#     print(i, end=" ")

# for i in range(len(lst)):
#     print(f"{i+ 1} -> {lst[i]}")

# for i in lst[::-1]:
#     print(i)

for i in range(len(lst ) - 1, -1, -1):
    print(lst[i])

print("====================")

i = len(lst)
while i:
    print(lst[i - 1])
    i -= 1
