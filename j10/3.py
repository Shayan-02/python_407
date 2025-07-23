s = 0
l = 0
mx = 0
while True:
    a = int(input())
    if a == -1:
        break
    else:
        if a > mx:
            mx = a
        s += a
        l += 1

av = s / l

if av == int(av):
    print(int(av))
else:
    print(av)

print(mx)