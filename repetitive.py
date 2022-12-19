from tkinter import filedialog
from tkinter import *
from tkinter import messagebox as mb
import time
def sav(text):
    d = filedialog.asksaveasfilename(initialdir="/",title=text,filetypes = (("Allfiles","*.*"),("TxT files","*.txt")))
    return d 
def add_file(text, types = (("Allfiles","*.*"),("TxT files","*.txt"))):
    d = filedialog.askopenfilename(initialdir="/",title=text,filetypes = types)
    return d
def ret_dir(text):
    d = filedialog.askdirectory(initialdir="/", title = text)
    return d