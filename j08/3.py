from random import choice

valid = ["سنگ", "کاغذ", "قیچی"]

user_score, computer_score = 0, 0

rounds = int(input("enter num of rounds: "))

for i in range(rounds):
    computer = choice(valid)
    user = input(f"round{i+1} -> enter your choice: ")
    if user == valid[0] or user == valid[1] or user == valid[2]:
        if user == computer:
            print("tie")
        else:
            if user == valid[0]:
                if computer == valid[1]:
                    print("computer win")
                    computer_score += 1
                else:
                    print("user win")
                    user_score += 1
            elif user == valid[1]:
                if computer == valid[2]:
                    print("computer win")
                    computer_score += 1
                else:
                    print("user win")
                    user_score += 1
            elif user == valid[2]:
                if computer == valid[0]:
                    print("computer win")
                    computer_score += 1
                else:
                    print("user win")
                    user_score += 1

print("user wins:", user_score, "\ncomputer score:", computer_score, "\ntie:", rounds-(user_score+computer_score))

if computer_score > user_score:
    print("winner: computer")
elif user_score > computer_score:
    print("winner : user")
else:
    print("tie")
