from tkinter import *
from tkinter import messagebox
from random import choice
import string as s

VALIDCHARS = s.ascii_lowercase + s.ascii_uppercase + s.punctuation + s.digits
BG_COLOR = "#4A71DD"
MAIN_FONT = ("vazir", 18, "bold")
SECOND_FONT = ("vazir", 14, "bold")

def generate_password():
    password = ""
    counter = int(counter_ent.get())
    for _ in range(counter):
        p = choice(VALIDCHARS)
        password += p
    password_lbl.config(text=password)

root = Tk()

root.title("password generator")
root.geometry("450x400")
root.resizable(False, False)
root.config(bg=BG_COLOR)

counter_lbl = Label(root, text="تعداد کاراکترها", font=MAIN_FONT, bg=BG_COLOR)
counter_lbl.pack(pady=20)

counter_ent = Entry(root, font=SECOND_FONT)
counter_ent.pack()

generate_btn = Button(root, text="ساخت رمز عبور", bg="#F5425A", font=MAIN_FONT, command= lambda : generate_password())
generate_btn.pack(pady=20)

password_lbl = Label(root, text="", bg=BG_COLOR, font=MAIN_FONT)
password_lbl.pack(pady=20)

root.mainloop()
