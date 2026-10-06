def isEven(num: int):
    # if num % 2 == 0: print(f"{num} is even")
    # else: print(f"{num} is odd")
    print(f"{num} is even" if num % 2 == 0 else f"{num} is odd")


isEven(4)
isEven(5)

isOdd = lambda num: f"{num} is even" if num % 2 == 0 else f"{num} is odd"

print(isOdd(4))
print(isOdd(5))