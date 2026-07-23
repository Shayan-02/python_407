start = int(input("enter start of range: "))
end = int(input("enter end of range: "))
i = start
while i <= end:
    print(i, end="\t")
    i += 3

print(f"\nstart: {start}\nend: {end}")