def fib(number:int) -> int:
    if number == 1 or number == 2:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)


print(fib(50))