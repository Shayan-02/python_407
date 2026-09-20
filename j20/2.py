def add_numbers(a, b):
    return f"{a} + {b} = {a + b}"


def subtract_numbers(a, b):
    return f"{a} - {b} = {a - b}"


def multiply_numbers(a, b):
    return f"{a} * {b} = {a * b}"


def divide_numbers(a, b):
    # if b == 0:
    #     return "can not divide by zero"
    try:
        return f"{a} / {b} = {a / b}"
    # except ZeroDivisionError:
    except Exception as e:
        return e



num1 = int(input("Enter first number: "))
op = input("Enter operation: ")
num2 = int(input("Enter second number: "))

if op == "+":
    print(add_numbers(num1, num2))
elif op == "-":
    print(subtract_numbers(num1, num2))
elif op == "*":
    print(multiply_numbers(num1, num2))
elif op == "/":
    print(divide_numbers(num1, num2))