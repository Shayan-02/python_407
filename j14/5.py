from random import choice

students = ["ali", "reza", "sara", "elmira", "amir", "fatemeh", "ahmad"]
valid = []

tedad = int(input("enter a number: "))

for i in students:
    if len(i) == tedad:
        valid.append(i)
        
correct = choice(valid)

print(correct)