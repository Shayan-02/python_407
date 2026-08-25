from tkinter import *


def show_fullname():
    fname = fname_ent.get()
    lname = lname_ent.get()
    fullname = fname + " " + lname
    fullname_lbl.config(text=f"{fullname}")


primary_font = ("vazir", 20, "bold")
secondary_font = ("vazir", 16, "bold")

window = Tk()

window.geometry("400x450")
window.resizable(False, False)

fname_lbl = Label(window, text="name", font=primary_font).place(x=20, y=20)
fname_ent = Entry(window, font=secondary_font, justify="center")
fname_ent.place(x=120, y=23)

lname_lbl = Label(window, text="family", font=primary_font).place(x=20, y=90)
lname_ent = Entry(window, font=secondary_font, justify="center")
lname_ent.place(x=120, y=93)

show_btn = Button(
    window, text="show name", font=primary_font, bg="#129832", command=show_fullname
)
show_btn.place(x=120, y=150)

fullname_lbl = Label(window, text="", font=primary_font)
fullname_lbl.place(x=70, y=250)

window.mainloop()
