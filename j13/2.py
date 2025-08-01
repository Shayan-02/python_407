from functools import reduce

def f(x):
    return 2 * x + 3


print(f(5))

f2 = lambda x: 2 * x + 3
print(f2(10))


def f3(x):
    pass


def func(x):
    return x > 5

def func(x):
    return x % 3

def func2(x):
    return x >= 5

li = [9, 10, 5, 1, 4, 2, 3, 4, 5, 6, 7]
li2 = [3, 2, 3]
sums = 0
mul = 1

for i in li:
    sums += i
    mul *= i

new = filter(func, li)
new2 = filter(func2, li)
print(li)  # -> [1, 9, 10, 5, 0, 4, 2, 3, 4, 5, 6, 7]
print(list(new))  # -> [1, 10, 5, 4, 2, 4, 5, 7]
print(list(new2))
new3 = filter(lambda x: x >= 5, li)
print(set(new3))
new4 = reduce(lambda x, y : x ** y, li2)
print(new4)
print(sums)
print(mul)
s = sorted(li, key=lambda x: x % 3)
print(s)