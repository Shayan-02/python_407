name = input("enter your firstname: ")
family = input("enter your lastname: ")
age = int(input("enter your age: "))

# way 1
print("Your first name is", name , ". your last name is", family, ".")
print("So your full name is", name, family, ".")
print("Your age is", age, "years old.")

print("-"*20)

# way 2
print(f"your name is {name}. your last name is {family}.")
print(f"So your full name is {name} {family}.")
print(f"Your age is {age} years old.")

print("*"*20)

# way 3
print("your name is {}. your last name is {}.".format(name, family))
print("So your full name is {} {}.".format(name, family))
print("Your age is {} years old.".format(age))