""" 
1 
voroodi nadarad 
khorooji nadarad
"""
def say_hello():
    print("hello world")

""" 
2
voroodi darad 
khorooji nadarad
"""
def say_hello2(name):
    print(f"hello {name}")

""" 
3
voroodi nadarad 
khorooji darad
"""
def say_hello3():
    return f"hello world"


""" 
4
voroodi darad 
khorooji darad
"""
def say_hello4(name):
    return f"hello {name}"


a = say_hello()
print(f"a -> {a}")

print("-"*40)

b = say_hello2("ali")
print(b)

print("-" * 40)

c = say_hello3()
print(f"{c} -> {type(c)}")

print("-"*40)
d = say_hello4("ali")
print(f"{d} -> {type(d)}")
