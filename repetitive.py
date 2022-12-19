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
def error(a):
    mb.showerror("Error",a)

