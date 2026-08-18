def sum_numbers(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"


def sub_numbers(num1, num2):
    return f"{num1} - {num2} = {num1 - num2}"


def mul_numbers(num1, num2):
    return f"{num1} * {num2} = {num1 * num2}"


def div_numbers(num1, num2):
    if number2:
        return f"{num1} / {num2} = {num1 / num2}"

number1 = int(input("enter number1: "))
operator = input("enter an operator: ")
number2 = int(input("enter number2: "))

if operator == "+":
    print(sum_numbers(number1, number2))
elif operator == "-":
    print(sub_numbers(number1, number2))
elif operator == "*":
    print(mul_numbers(number1, number2))
elif operator == "/":
    if number2 == 0:
        "Can't divide by zero"
    else:
        print(div_numbers(number1, number2))
