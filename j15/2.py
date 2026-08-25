from tkinter import *


def show_fullname():
    fname = fname_ent.get()
    lname = lname_ent.get()
    fullname = fname + " " + lname
    fullname_lbl.config(text=f"your fullname is {fullname}")


primary_font = ("vazir", 20, "bold")
secondary_font = ("vazir", 16, "bold")

window = Tk()

window.geometry("500x500")
window.resizable(False, False)

fname_lbl = Label(window, text="name", font=primary_font).grid(row=0, column=0, pady=10, padx=10)
fname_ent = Entry(window, font=secondary_font, justify="center")
fname_ent.grid(row=0, column=1, pady=10)

lname_lbl = Label(window, text=" family", font=primary_font).grid(row=1, column=0, pady=10, padx=10)
lname_ent = Entry(window, font=secondary_font, justify="center")
lname_ent.grid(row=1, column=1, pady=10)

show_btn = Button(
    window, text=" show fullname", font=primary_font, bg="#129832", command=show_fullname
)
show_btn.grid(row=2, column=1, pady=20)

fullname_lbl = Label(window, text="", font=primary_font)
fullname_lbl.grid(row=3, column=1)

window.mainloop()
