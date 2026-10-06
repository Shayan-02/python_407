class Person:
    def __init__(self, name, pid, age, sex=""):
        self.name = name
        self.pid = pid
        self.age = age
        self.sex = sex
    def eat(self, food):
        return f"{self.name} is eating {food}"
    def info(self):
        return f"""my name is {self.name}
my age is {self.age} years old.
    """
    


class Student(Person):
    def __init__(self, name, pid, age, major="", grade=0):
        super().__init__(name, pid, age)
        self.major = major
        self.grade = grade
    def eat(self, food):
        return super().eat(food) + " in school"


s1 = Student(pid="0987654321", name="ali", age=20)
s2 = Student("ali", "0123456789", 22)

print(s1.eat("sandwiches"))