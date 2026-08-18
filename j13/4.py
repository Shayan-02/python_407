def fact(number: int) -> int:
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return f"factoraial of {number} is {fact}"


a = int(input("enter a number: "))
print(fact(a))