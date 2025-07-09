correct = 50

level = int(input("""
enter game level (1-3):
1: easy
2: medium
3: advanced
"""))

if level == 1:
    i = 5
elif level == 2:
    i = 4
elif level == 3:
    i = 3
else:
    print("invalid input")

temp = i

print(f"you have {i} chances")

while temp:
    n = i - temp + 1
    guess = int(input(f"enter your chance{n}: "))
    if guess == correct:
        print("you win")
        break
    elif guess > correct:
        print("too high")
    else:
        print("too low")
    temp -= 1
    print(f"you have {i - n} another chances")
else:
    print("game over")