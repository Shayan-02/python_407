# inputs
# start = int(input("enter start: "))
# end = int(input("enter end: "))
start = 1
end = 20
temp = end

while start <= end:
    if start == 18:
        print("inja break shode")
        break
    elif start == 8 or start == 14:
        start += 1
        continue
    print(start)
    start += 1