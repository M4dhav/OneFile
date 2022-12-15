from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import Button
from PIL import ImageTk, Image
from madhav import encryption as e
from madhav import decryption as d
from save import add_file
import img_grabber
from tkinter import messagebox as mb
root = Tk()
root.geometry("900x550")
root.maxsize(900,550)
root.minsize(900,550)
root.title("OneFile")

def new():
    top = Toplevel()
    top.geometry("300x150")
    top.maxsize(300,150)
    top.minsize(300,150)
    def fil():
        print(file_n.get())
    file_n = StringVar()
    file_e = Entry(top,textvariable=file_n)
    file_e.place(x=75,y = 50)
    lbl = Label(top,text='''Enter file format (should be zip,bztar,gztar,xztar)''').place(x=35,y=15)
    b = Button(top,text = "SUBMIT",command=fil)
    b.place(x=110,y = 75)

    top.mainloop()


img = ImageTk.PhotoImage(file = 'logo.png')
root.iconphoto(False,img)

root["background"]= "#09203F"
root.attributes("-alpha",0.95)

bg  = Image.open(r"logo.png")
cop = bg.resize((250,250),Image.Resampling.LANCZOS)
decomp = ImageTk.PhotoImage(cop)
label = Label(root,image = decomp)
label.place(x=330,y=50)

text = "Select a file"

def compress():
    new()
comp = ImageTk.PhotoImage(file=r"compress.png")
b2 = Button(root,command=compress,height = 100,width = 100,image=comp)
b2.place(x=100, y=375)




def decompress():
    pass
decmp = ImageTk.PhotoImage(file=r"decompress.png") 
b3 = Button(root,command=decompress,height = 100,width = 100,image=decmp)
b3.place(x=300,y=375)



def encrypt():
    e(add_file(text))
    # sav()
encrp = ImageTk.PhotoImage(file=r"encrypt.png")
b4 = Button(root,text="ENCRYPT",command=encrypt,height = 100,width = 100,image=encrp)
b4.place(x=500,y=375)




def decrypt():
    d(add_file(text))
decrp = ImageTk.PhotoImage(file=r"decrypt.png")
b5 = Button(root,text="DECRYPT",command=decrypt,height = 100,width = 100,image=decrp)
b5.place(x=700, y=375)


root.mainloop()