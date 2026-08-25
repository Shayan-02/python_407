from tkinter import *

root = Tk()

bg = "#622FDA"

root.title("first app")
root.geometry("500x500")
root.resizable(0, 0)
root.config(bg=bg)

lbl = Label(root, text="سلام این اولین نرم افزار گرافیکی است", bg= bg, fg="white", font=('vazir', 20, 'bold')).pack()

root.mainloop()
