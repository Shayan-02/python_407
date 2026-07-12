a = int(input("enter a number: "))

yekan = a % 10
dahgan = a // 10

sum_numbers = yekan + dahgan
reversed_numbers = int(str(yekan) + str(dahgan))

print(f"majmoo argham -> {sum_numbers}")
print(f"maghloobe adad -> {reversed_numbers}")

print("="*20)

print(a is reversed_numbers)
print(a == reversed_numbers)