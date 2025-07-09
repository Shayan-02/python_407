# inputs
start = int(input("enter start: "))
end = int(input("enter end: "))
temp = end

# loop
if start >= end:
    print("ghalat vared kardi")
else:
    while temp >= start:
        if temp % 3 == 0 and temp % 5 != 0:
            print(temp)
        temp -= 1