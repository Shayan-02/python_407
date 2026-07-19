# n = 3

# user = int(input("enter a number: "))

# if user == n:
#     print("you win")
# else:
#     if user > n:
#         print("enter lower number")
#     else:
#         print("enter bigger number")

n = 20
user = int(input("enter a number: "))

if user == n:
    print("you win")
elif user > n:
    print("enter lower number")
elif user < n: # else:
    print("enter bigger number")
