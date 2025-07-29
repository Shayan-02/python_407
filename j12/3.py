def mosalas(a, b, c):
    s = a + b + c
    if s == 180 and 360 > a > 0 and 360 > b > 0 and 360 > c > 0:
        print("Yes")
    else:
        print("No")


zaveh = input().split()
x = int(zaveh[0])
y = int(zaveh[1])
z = int(zaveh[2])

mosalas(x, y, z)