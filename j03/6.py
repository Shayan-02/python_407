a = int(input("enter a number: "))

yekan = a % 10
dahgan = a // 10

reversed_numbers = int(str(yekan) + str(dahgan))

print(f"maghloobe adad -> {reversed_numbers}")

if yekan == dahgan:
    print("adad khod maghloob ast")
    print("salam")
else:
    print("adad khod maghloob nist")