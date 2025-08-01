# from random import randint
# from random import choice
import random as r
def guessNumber(start, end, choice):
    c = r.randint(start, end)
    if choice == c:
        print("you win")
    elif choice < c:
        print("lower")
    elif choice > c:
        print("higher")

def main(rounds):
    for i in range(rounds):
        

rounds = int(input("enter rounds: "))
start = int(input("enter start: "))
end = int(input("enter end: "))
