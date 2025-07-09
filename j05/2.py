s = 0
t = 0
for i in range(4):
    a = int(input("enter a number: "))
    if 0 > a or a > 20:
        print("invalid number")
    else:
        s += a
        t += 1

avg = s / t

if avg >= 16:
    print("avg:", avg, "grade: A")
elif avg >= 14:
    print("avg:", avg, "grade: B")
elif avg >= 12:
    print("avg:", avg, "grade: C")
elif avg >= 10:
    print("avg:", avg, "grade: D")
elif avg < 10:
    print("avg:", avg, "grade: Fail")