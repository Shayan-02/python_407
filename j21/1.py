import datetime

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = datetime.datetime.now().year
        age = current_year - birth_year
        return cls(name, age)

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# استفاده از متد معمولی
emp1 = Employee("Alice", 30)
emp1.display_info()

# استفاده از classmethod
emp2 = Employee.from_birth_year("Bob", 1995)
emp2.display_info()