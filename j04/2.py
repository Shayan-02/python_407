a = int(input("enter a number: "))

if a % 2 == 0:
    print("even")
else:
    print("odd")

r = "even" if a % 2 == 0 else "odd"
print(r)