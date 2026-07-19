correct_number = 20

chances = 3
start = 1
end = 50
while chances > 0:
    guess = int(input(f"choose a number between {start} and {end}: "))
    if start <= guess <= end:
        if correct_number == guess:
            print("you win")
            break
        else:
            if correct_number > guess:
                print("enter bigger number")
            else:
                print("enter lower number")
        chances -= 1
    else:
        print(f"enter valid number betwwen {start} and {end}")
else:
    print("Game Over")