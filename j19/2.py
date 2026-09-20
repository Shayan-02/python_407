class BankAccount:
    def __init__(self, name, pid, balance):
        self._name = name
        self.pid = pid
        self.__balance = balance

    def get_balance(self):
        return f"balance is {self.__balance}"
    
    def get_info(self):
        return f"name : {self._name}\npid : {self.pid}\nbalance : {self.__balance}"
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("amount must be higher than 0")
    
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("not enough balance")
    
    # def update_info(self, value, type):
    #     if type == "name":
    #         self.name = value
    #     elif type == "pid":
    #         self.pid = value

    def set_balance(self, balance):
        self.__balance = balance


b1 = BankAccount("ali", "0987654321", 500)

print(b1.get_balance())
print(b1.get_info())


# b1.update_info(type="name", value="reza")
# print(b1.show_info())

b1.deposit(-500)
print(b1.get_balance())
b1.deposit(300)
print(b1.get_balance())

b1.withdraw(1400)
print(b1.get_balance())
b1.withdraw(200)
print(b1.get_balance())

b1._name = "reza"

print(b1.get_info())

b1.set_balance(1500)

print(b1.get_balance())