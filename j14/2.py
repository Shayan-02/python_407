from random import randint

start = int(input("enter start range: "))
end = int(input("enter end range: "))

correctnumber = randint(start, end)

for i in range(5):
    guess = int(input(f"enter a number between {start} and {end}: "))
    if guess == correctnumber:
        print("you win")
        break
    elif guess < correctnumber:
        print("enter higher number")
    else:
        print("enter lower number")
else:
    print(f"game over\ncorrect number was {correctnumber}")