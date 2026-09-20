class Person:
    def __init__(self, name, age, pid):
        self.name = name
        self.age = age
        self.pid = pid
    
    def info(self):
        return f"""name : {self.name}\nage : {self.age}\npid : {self.pid}"""
    
    
p1 = Person(age=20, name="ali", pid="0987654321")

print(p1.info())