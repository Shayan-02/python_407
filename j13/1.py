def average(*a):
    valid = []
    for i in a:
        if 0 <= int(i) <= 20:
            valid.append(int(i))
        else:
            print("invalid number")
    av = sum(valid) / len(valid)
    if av >= 18:
        return av + " " + "A"
    elif av >= 16:
        return str(av) + " " + "B"
    elif av >= 14:
        return str(av) + " " + "C"
    elif av >= 10:
        return str(av) + " " + "D"
    else:
        return str(av) + " " + "Failed"


# lst = []
# while True:
#     number = int(input("enter your number: "))
#     if number == -1:
#         break
#     else:
#         lst.append(number)


# print(average(lst))

print(average(input()))