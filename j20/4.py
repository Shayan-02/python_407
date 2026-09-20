from tkinter import messagebox


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            # raise ValueError("You don't have enough money to withdraw")
            messagebox.showerror("Error", "You cannot withdraw more than you have")
        else:
            self.balance -= amount
    def deposit(self, amount):
        self.balance += amount
    def show_balance(self):
        return f"Balance: {self.balance}"


b1 = BankAccount(100)
b1.withdraw(1000)
print(b1.show_balance())