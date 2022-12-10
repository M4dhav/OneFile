import os
from cryptography.fernet import Fernet
def encryption(filepath,key = None):
    try:
        filename = ""
        fileexten = ""
        for i in filepath[::-1]:
            if i == chr(92):
                break
            filename += i
        for i in filepath[::-1]:
            if i == ".":
                break
            fileexten += i
        fileexten = fileexten[::-1]
        filename = filename[::-1]
        filename = filename.replace(".","")
        filename += "_encrypted"
        filename += "." + fileexten
        print(filename)
        if key == None:
            key = Fernet.generate_key()
        else:
            key = key
        choice = input("Do you want a new encrypted copy of the file or for the current copy to be encrypted?(New/Current)\n")
        if choice == "New" or choice == "new":
            with open(filepath,"rb") as file:
                content = file.read()
            content = Fernet(key).encrypt(content)
            with open(filename.txt,"wb") as file:
                file.write(content)
    except FileNotFoundError:
        print("Please enter a valid file location.")
encryption(input())