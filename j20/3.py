a = 10
b1 = 0

try:
    c = a / b
    print(c)
# except ZeroDivisionError:
#     print("can not divide by zero")
# except NameError:
#     print("you must enter two numbers")
except Exception as e:
    print(e)