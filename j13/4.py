def fibonachi(n):
    valid = []
    if n == 1 or n == 2:
        return 1
    else:
        m = fibonachi(n-1) + fibonachi(n-2)
        valid.append(m)
        return valid


print(fibonachi(1))
print(fibonachi(2))
print(fibonachi(3))
print(fibonachi(4))
print(fibonachi(5))
print(fibonachi(6))
print(fibonachi(7))