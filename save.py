from tkinter import filedialog
from tkinter import *
from tkinter import messagebox as mb
import time
def sav(text):
    d = filedialog.asksaveasfilename(initialdir="/",title=text,filetypes = (("Allfiles","*.*"),("TxT files","*.txt")))
    return d 
def add_file(text):
    d = filedialog.askopenfilename(initialdir="/",title=text,filetypes = (("Allfiles","*.*"),("TxT files","*.txt")))
    return d
def ret_dir():
    d = filedialog.askdirectory(initialdir="/", title = "Enter directory to be unzipped to")
    return d
# def rot():
#     def dest():
#         top.destroy()
#     def both1():
#         dest()
#         return (1)
#     def both2():
#         dest()
#         return (0)
    # top = Toplevel()
    # top.geometry("300x200")
    # top.minsize(300,180)
    # top.maxsize(300,180)
    # label = Label(top,text='''Do you want a new encrypted copy of the file or
    # for the current copy to be encrypted?''')
    # label.place(x=25,y=0)


    # b9 = Button(top,text = "NEW",font =("",8,"bold"),height = 2,width = 8 ,command=both1)
    # b9.place(x =80 ,y=70)


    # b2 = Button(top,text = "CURRENT",font =("",8,"bold"),height = 2, width=8,command=both2)
    # b2.place(x=170,y=70)
    # top.mainloop()
def error(a):
    mb.showerror("Error",a)

