from tkinter import *


def show_fullname():
    fname = fname_ent.get()
    lname = lname_ent.get()
    fullname = fname + " " + lname
    fullname_lbl.config(text=f"نام کامل شما {fullname} است")


primary_font = ('vazir', 20, 'bold')
secondary_font = ('vazir', 16, 'bold')

window = Tk()

window.geometry("400x450")
window.resizable(False, False)

fname_lbl = Label(window, text="نام", font=primary_font).pack(pady=15)
fname_ent = Entry(window, font=secondary_font, justify="center")
fname_ent.pack()

lname_lbl = Label(window, text="نام خانوادگی", font=primary_font).pack(pady=15)
lname_ent = Entry(window, font=secondary_font, justify="center")
lname_ent.pack()

show_btn = Button(window, text="نمایش نام", font=primary_font, bg="#129832", command=show_fullname)
show_btn.pack(pady=20)

fullname_lbl = Label(window, text="", font=primary_font)
fullname_lbl.pack()

window.mainloop()