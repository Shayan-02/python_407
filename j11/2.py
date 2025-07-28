from tkinter import *

root = Tk()
root.configure(background="blue")

lbl = Label(root, text="hello world").grid(row=0, column=0)

root.mainloop()