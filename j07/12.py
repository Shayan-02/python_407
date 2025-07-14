lst = []
lst2 = []

while 1:
    a = int(input())
    if a == 0:
        break
    else:
        lst.append(a)


# for _ in lst:
#     lst2.insert(0, _)

# lst2 = lst.reverse()

for _ in lst[::-1]:
# for _ in lst2:
    print(_)