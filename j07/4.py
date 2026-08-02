a = int(input("enter a number: "))

b = ""
for i in range(len(str(a))):
    b += str(a)[i]

# if b == a:
#     print("yes")
# else:
#     print("no")

print("yes" if int(b) == a else "no")