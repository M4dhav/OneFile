from tkinter import filedialog
def sav():
    d = filedialog.asksaveasfilename(initialdir="/",title="Save file",filetypes = (("Allfiles","*.*"),("TxT files","*.txt")))
    return d 
def add_file(text):
    d = filedialog.askopenfilename(initialdir="/",title=text,filetypes = (("Allfiles","*.*"),("TxT files","*.txt")))
    return d 