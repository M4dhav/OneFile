from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import Button
from PIL import ImageTk, Image
from madhav import encryption as e
from madhav import decryption as d
from save import add_file

root = Tk()
root.geometry("900x550")
root.maxsize(900,550)
root.minsize(900,550)
root.title("OneFile")


root["background"]= "#4B4340"


text = "Select a file"

def compress():
    pass
image = Image.open(r"C:\Users\Dell\Documents\GitHub\end-sem-hackathon-proj\end-sem-hackathon-project\compress_icon.jpg")
cop = image.resize((150,100),Image.Resampling.LANCZOS)
comp = ImageTk.PhotoImage(cop)
b2 = Button(root,command=compress,height = 100,width = 150,image=comp)
b2.place(x=60, y=300)
lbl1 = Label(root,text="COMPRESS",font=("",10,"bold")).place(x=100,y=410)



def decompress():
    pass

image = Image.open(r"C:\Users\Dell\Documents\GitHub\end-sem-hackathon-proj\end-sem-hackathon-project\decompress_icon.jpg")
cop = image.resize((150,100),Image.Resampling.LANCZOS)
decomp = ImageTk.PhotoImage(cop)
b3 = Button(root,command=decompress,height = 100,width = 150,image=decomp)
b3.place(x=270,y=300)
lbl2 = Label(root,text="DECOMPRESS",font=("",10,"bold")).place(x=300,y=410)



def encrypt():
    e(add_file(text))
image = Image.open(r"C:\Users\Dell\Documents\GitHub\end-sem-hackathon-proj\end-sem-hackathon-project\encrpyt_icon.jpg")
cop = image.resize((150,100),Image.Resampling.LANCZOS)
encrp = ImageTk.PhotoImage(cop)
b4 = Button(root,text="ENCRYPT",command=encrypt,height = 100,width = 150,image=encrp)
b4.place(x=480,y=300)
lbl1 = Label(root,text="ENCRYPT",font=("",10,"bold"))
lbl1.place(x=530,y=410)



def decrypt():
    d(add_file(text))
image = Image.open(r"C:\Users\Dell\Documents\GitHub\end-sem-hackathon-proj\end-sem-hackathon-project\decrypt_icon.jpg")
cop = image.resize((150,100),Image.Resampling.LANCZOS)
decrp = ImageTk.PhotoImage(cop)
b5 = Button(root,text="DECRYPT",command=decrypt,height = 100,width = 150,image=decrp)
b5.place(x=690, y=300)
lbl1 = Label(root,text="DECRYPT",font=("",10,"bold")).place(x=740,y=410)
  



root.mainloop()