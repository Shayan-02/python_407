fname = input("enter your first name: ")
lname = input("enter your last name: ")
age = int(input("enter your age: "))

print("your firstname is", fname, "\nyour lastname is", lname, "\nyour age is", age, "years old", "\nso your fullname is", fname, lname)

print("--------------------------------------------------")

print(f"your firstname is {fname} \nyour lastname is {lname} \nyour age is {age} years old \nso your fullname is {fname} {lname}")

print("--------------------------------------------------")

print("your firstname is {} \nyour lastname is {} \nyour age is {} years old \nso your fullname is {} {}".format(fname, lname, age, fname, lname))

print("--------------------------------------------------")