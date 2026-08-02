number = int(input())

fact = 1
for i in range(1, number + 1, 1):
    fact *= i

# i = 1
# while i <= number:
#     fact *= i
#     i += 1

print(fact)