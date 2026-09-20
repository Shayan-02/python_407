a = "10"
b = 1

while True:
    print("salam")

try:
    c = a / b
    print(c)
# except ZeroDivisionError:
#     print("can not divide by zero")
# except NameError:
#     print("you must enter two numbers")
except Exception as e:
    print(e)
finally:
    print("finally end")