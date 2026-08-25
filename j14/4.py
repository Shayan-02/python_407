from random import randint

start = int(input("enter start range: "))
end = int(input("enter end range: "))
correctnumber = randint(start, end)


def guess_number( number):
    global iswin
    iswin = False
    # global correctnumber
    if number == correctnumber:
        iswin = True
        print("you win")
        return
    else:
        if number < correctnumber:
            return "enter higher number"
        else:
            return "enter lower number"


i = 1
while i <= 5:
    guess = int(input(f"guess {i}\nenter a number: "))
    if start <= guess <= end:
        result = guess_number(guess)
        if iswin == True:
            break
        else:
            print(result)
        i += 1
    else:
        print(f"enter valid number in range {start} and {end}")
else:
    print("game over")