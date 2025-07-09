start = int(input("start: "))
end = int(input("end: "))

for i in range(end, start-1, -1):
    if i % 3 == 0 and i % 5 != 0:
        print(i, end="\t")