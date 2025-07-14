n = int(input("enter a number: "))
m = int(input("enter a number: "))

i = 1
j = 1

while i <= n:
    j = 1
    while j <= m:
        print(i*j, end="\t")
        j += 1
    print()
    i += 1