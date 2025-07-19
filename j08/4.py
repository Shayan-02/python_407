from random import randint

start = int(input("start: "))
end = int(input("end: "))

correct = randint(start, end)

i = 1
while i <= 5:
    guess = int(input(f"guess {i} -> enter a number: "))
    if guess == correct:
        print(f"you win in {i} rounds")
        break
    else:
        if guess > correct:
            print("too high")
        else:
            print("too low")
        print(f"you have {5-i} another chances")
        i += 1
else:
    print("game over!", "\ncorrect:", correct)