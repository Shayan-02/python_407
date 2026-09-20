class Alive:
    def __init__(self, height):
        self.height = height


class Person(Alive):
    def __init__(self, height, name, age):
        super().__init__(height)
        self.name = name
        self.age = age


    def speak(self):
        return f"{self.name} is speaking"

    def sleep(self):
        return f"{self.name} is sleeping"
    def info(self):
        return f" name is {self.name} and my age is {self.age}"




class Student(Person):
    def __init__(self, height, name, age, job):
        super().__init__(height, name, age)
        self.job = job
    def info(self):
        return "my" + super().info() + " years old."

class Employee(Person):
    def __init__(self, height, name, age, sabegheh, job):
        super().__init__(height, name, age)
        self.sabegheh = sabegheh
        self.job = job

    def info(self):
        return "my" + super().info() + " years old."

class Baby(Person):
    def __init__(self, height, name, age):
        super().__init__(height, name, age)
    def info(self):
        return "my child" + super().info() + " months old."

s1 = Student(170, "reza", 20, "studding")
print(s1.speak())
print(s1.sleep())
print(s1.info())
print(s1.height)

e1 = Employee(180, "ali", 30, 10, "computer")
print(e1.speak())
print(e1.sleep())
print(e1.height)
print(e1.info())

b1 = Baby(90, "sara", 11)
print(b1.info())
