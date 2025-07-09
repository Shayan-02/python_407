a = 10
b = 20
c = 30

if a >= b and b >= c:
    print(1)
elif a < b > c:
    print(2)
elif a > b < c:
    print(3)
elif a < b < c:
    print(4)

print("--------")

if a > b or b > c:
    print("A")
# elif a > b or b < c:
#     print("B")
elif a > b or b > c:
    print(c)
elif a < b or b < c:
    print("D")