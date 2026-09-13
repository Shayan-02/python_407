class User:
    def __init__(self, name, age):
        self.esm = name
        self.sen = age

    def sleep(self):
        return f"{self.esm} is sleeping.😴"

    def info(self):
        return f"user name is {self.esm}\nuser age is {self.sen}"


u1 = User("reza", 20)
print(u1.esm)
print(u1.sen)
print(u1.sleep())
print(u1.info())