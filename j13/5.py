def fact(number: int) -> int:
    if number == 1:
        return 1
    else:
        return number * fact(number - 1)


a = int(input("enter a number: "))
print( f"factoraial of {a} is {fact(a)}")
