run = True

sumNumbers = 0
length = 0
while run:
    number = float(input("enter a number: "))
    if number < 0:
        run = False
    else:
        sumNumbers += number
        length += 1


avg = sumNumbers / length
print("avg: ", avg)