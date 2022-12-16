import shutil
from save import add_file
from save import sav
from save import ret_dir
from tkinter import *
from save import error
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
    filename = add_file("Select File to be unarchived")

    # Target directory
    extract_dir = ret_dir()

    # Format of archive file
    archive_format = new()

    # Unpack the archive file
    shutil.unpack_archive(filename, extract_dir, archive_format)
    print("Archive file unpacked successfully.")

#make archive function
def ma():
    filename = add_file("Select File to be archived")
    newname= ret_dir()
    new()
    global var
    formatf = var
    # print(formatf)
    shutil.make_archive(newname,formatf,filename)
    

