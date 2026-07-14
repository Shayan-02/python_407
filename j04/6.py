a = 10
b = 20
c = 30

if a > b and b < c:
    print("one")
elif a < b and b > c:
    print("tow")
elif a < b and b == c:
    print("three")
else:
    print("nothing")

if a > b or b > c:
    print("one")
elif a < b or b > c: print("tow")