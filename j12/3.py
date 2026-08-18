def calc(number1, number2, operator):
    if operator == "+":
        print(f"{number1} + {number2} = {number1 + number2}")
    elif operator == "-":
        print(f"{number1} - {number2} = {number1 - number2}")
    elif operator == "*":
        print(f"{number1} * {number2} = {number1 * number2}")
    elif operator == "/":
        if number2:
            print(f"{number1} - {number2} = {number1 - number2}")
        else:
            print("Can't divide by zero")


number1 = int(input("enter number1: "))
operator = input("enter an operator: ")
number2 = int(input("enter number2: "))

calc(number1, number2, operator)