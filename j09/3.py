lst1 = [1, 2, 3, 4]
lst2 = [6, 7, 8 , 9, 10]

lst1.append(5)
lst1.insert(0, "salam")

# lst1.append(lst2)

# for i in lst2:
#     lst1.append(i)

lst1.extend(lst2)

print(lst1)