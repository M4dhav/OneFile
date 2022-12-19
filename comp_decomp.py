import shutil
import os
from repetitive import add_file
from repetitive import sav
from repetitive import ret_dir
from tkinter import *
from repetitive import error
var = None
def new():
    top = Toplevel()
    top.geometry("300x150")
    top.maxsize(300,150)
    top.minsize(300,150)
    def fil(): 
        top.destroy()
        global var
        var = clicked.get()
        top.quit()
  
    options = ["zip", "bztar", "gztar", "xztar"]
    clicked = StringVar()
    clicked.set("zip")
    drop = OptionMenu(top , clicked,*options)
    drop.place(x=105,y=40)
    lbl = Label(top,text='''Select file format (should be zip,bztar,gztar,xztar)''').place(x=20,y=15)
    b = Button(top,text = "SUBMIT",command=fil)
    b.place(x=110,y = 75)

    top.mainloop()

'''COMPRESSION FUNCTIONS'''
def uz():
    # Full path of
    # the archive file
    filename = add_file("x")

    # Target directory
    #print(filename.split('/')[-1].split('.')[0])
    extract_dir = ret_dir()+'/'+filename.split('/')[-1].split('.')[0]
    os.mkdir(extract_dir)
    #print(extract_dir+filename.split('/')[-1].split('.')[0])


    # Format of archive file
    new()
    global var
    archive_format = var
    #print(filename)
    #print(extract_dir)
    #print(archive_format)

    # Unpack the archive file
    shutil.unpack_archive(filename, extract_dir, archive_format)
    #shutil.unpack_archive('C:\Users\Dell\Desktop\New folder\PYTHON.zip','C:\Users\Dell\Documents\PYTHON','zip')

#make archive function
def ma():
    filename = ret_dir()
    #print(filename)
    newname= ret_dir()+'/'+filename.split('/')[-1]
    #print(newname)
    new()
    global var
    formatf = var
    # print(formatf)
    shutil.make_archive(newname,formatf,filename)
    

