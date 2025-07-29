def number(n):
    if n % 2 == 0:
        print(n)

a = input().split()
start = int(a[0])
end = int(a[1])
for i in range(start, end+1):
    number(i)