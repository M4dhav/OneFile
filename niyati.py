from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import Button
from PIL import ImageTk, Image
from madhav import encryption as e
from madhav import decryption as d
from save import add_file
import img_grabber
root = Tk()
root.geometry("900x550")
root.maxsize(900,550)
root.minsize(900,550)
root.title("OneFile")

img = ImageTk.PhotoImage(file = 'logo.png')
root.iconphoto(False,img)

# root["background"]= "#325984"
root["background"]= "#1d324b"
# root["background"]= "#627183"
# bg = ImageTk.PhotoImage(file= r"C:\Users\Dell\Desktop\Hackathon\bg.png")

text = "Select a file"


    # print(d)
# b1 = Button(root,text="CHOOSE A FILE",font=("times",10,"bold"),command=add_file)
# b1.pack(pady=177,fill=BOTH , padx=350)


def compress():
    # sav()
    pass
comp = ImageTk.PhotoImage(file=r"compress.png")
b2 = Button(root,command=compress,height = 100,width = 150,image=comp)
b2.place(x=60, y=300)
lbl1 = Label(root,text="COMPRESS",font=("",10,"bold")).place(x=100,y=410)

def decompress():
    # sav()
    pass
decmp = ImageTk.PhotoImage(file=r"decompress.png") 
b3 = Button(root,command=decompress,height = 100,width = 150,image=decmp)
b3.place(x=270,y=300)
lbl2 = Label(root,text="DECOMPRESS",font=("",10,"bold")).place(x=300,y=410)


def encrypt():
    e(add_file(text))
    # sav()
encrp = ImageTk.PhotoImage(file=r"encrypt.png")
b4 = Button(root,text="ENCRYPT",command=encrypt,height = 100,width = 150,image=encrp)
b4.place(x=480,y=300)
lbl1 = Label(root,text="ENCRYPT",font=("",10,"bold")).place(x=530,y=410)



def decrypt():
    d(add_file(text))
    # sav()
decrp = ImageTk.PhotoImage(file=r"decrypt.png")
b5 = Button(root,text="DECRYPT",command=decrypt,height = 100,width = 150,image=decrp)
b5.place(x=690, y=300)
lbl1 = Label(root,text="DECRYPT",font=("",10,"bold")).place(x=740,y=410)


#     filedialog.asksaveasfile(initialfile = 'Untitled',
# defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])




root.mainloop()