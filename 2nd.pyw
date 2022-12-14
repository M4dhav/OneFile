from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import Button
from PIL import ImageTk, Image


root = Tk()
root.geometry("900x550")
root.maxsize(900,550)
root.minsize(900,550)
root.title("OpenFile")

img = ImageTk.PhotoImage(file = 'C:\\Users\\Dell\\Desktop\\Hackathon\\ico.png')
root.iconphoto(False,img)

# root["background"]= "#325984"
root["background"]= "#1d324b"
# root["background"]= "#627183"
# bg = ImageTk.PhotoImage(file= r"C:\Users\Dell\Desktop\Hackathon\bg.png")



def add_file():
    d = filedialog.askopenfilename(initialdir="/",title="Select a file",filetypes = (("Allfiles","*.*"),("TxT files","*.txt")))
    # print(d)
b1 = Button(root,text="CHOOSE A FILE",font=("times",10,"bold"),command=add_file)
b1.pack(pady=177,fill=BOTH , padx=350)


def compress():
    sav()
comp = ImageTk.PhotoImage(file=r"C:\Users\Dell\Desktop\Hackathon\compress.png")
b2 = Button(root,command=compress,height = 100,width = 150,image=comp)
b2.place(x=60, y=300)
lbl1 = Label(root,text="COMPRESS",font=("",10,"bold")).place(x=100,y=410)

def decompress():
    sav()
decmp = ImageTk.PhotoImage(file=r"C:\Users\Dell\Desktop\Hackathon\2528903.png") 
b3 = Button(root,command=decompress,height = 100,width = 150,image=decmp)
b3.place(x=270,y=300)
lbl2 = Label(root,text="DECOMPRESS",font=("",10,"bold")).place(x=300,y=410)


def encrypt():
    sav()
encrp = ImageTk.PhotoImage(file=r"C:\Users\Dell\Desktop\Hackathon\625728.png")
b4 = Button(root,text="ENCRYPT",command=encrypt,height = 100,width = 150,image=encrp)
b4.place(x=480,y=300)
lbl1 = Label(root,text="ENCRYPT",font=("",10,"bold")).place(x=530,y=410)



def decrypt():
    sav()
decrp = ImageTk.PhotoImage(file=r"C:\Users\Dell\Desktop\Hackathon\DFD-Decryption.webp")
b5 = Button(root,text="DECRYPT",command=decrypt,height = 100,width = 150,image=decrp)
b5.place(x=690, y=300)
lbl1 = Label(root,text="DECRYPT",font=("",10,"bold")).place(x=740,y=410)

def sav():
    filedialog.asksaveasfile(initialfile = 'Untitled',
defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])




root.mainloop()