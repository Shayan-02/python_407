
i = int(input())
while i:
    step = 1
    print(f"round{i}")
    user1 = input("enter your chance: ")
    user2 = input("enter your chance: ")
    if (user1 == "sang" and user2 == "kaghaz") or (user1 == "gheichi" and user2 == "sang") or (user1 == "kaghaz" and user2 == "gheicchi"):
        print("user2 win")
    elif (user2 == "sang" and user1 == "kaghaz") or (user2 == "gheichi" and user1 == "sang") or (user2 == "kaghaz" and user1 == "gheicchi"):
        print("user1 win")
    else:
        print("draw")
    i -= 1
    step += 1