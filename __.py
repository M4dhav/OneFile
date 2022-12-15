from tkinter import *
from tkinter import filedialog
def fil():
    print(file_n.get())
root = Tk()
root.geometry("400x400")
file_n = StringVar()
file = Entry(root,textvariable=file_n).pack()


root.mainloop()
