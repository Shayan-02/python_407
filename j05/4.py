start = int(input("enter start range: "))
end = int(input("enter end range: "))

while start <= end:
    if start % 15 == 0:
        print(f"{start} -> fizzbazz")
    elif start % 5 == 0:
        print(f"{start} -> bazz")
    elif start % 3 == 0:
        print(f"{start} -> fizz")
    else:
        print(start)
    start += 1