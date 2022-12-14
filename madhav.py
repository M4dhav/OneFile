import os
from cryptography.fernet import Fernet
from save import sav
from save import add_file
def encryption(filepath):
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
        filename = filename.replace(fileexten, "")
        filename += "_encrypted"
        filename += "." + fileexten
        key = Fernet.generate_key()
        key_path = sav()
        with open(key_path, "wb") as key_file:
            key_file.write(key)
        # choice = input("Do you want a new encrypted copy of the file or for the current copy to be encrypted?(New/Current)\n")
        # possible_inputs = ["New", "new", "Current", "current"]
        # while choice not in possible_inputs:
        #     print("Please enter a valid choice.\n")
        #     choice = input("Do you want a new encrypted copy of the file or for the current copy to be encrypted?(New/Current)\n")
        with open(filepath,"rb") as file:
            content = file.read()
        content_encrypted = Fernet(key).encrypt(content)
        # if choice == "New" or choice == "new":
        #     with open(filename,"wb") as file:
        #         file.write(content_encrypted)
        # else:
        with open(sav(), "wb") as file:
            file.write(content_encrypted)
    except FileNotFoundError:
        print("Please enter a valid file location.")

def decryption(filepath):
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
        filename = filename.replace(fileexten, "")
        filename = filename.replace("_encrypted", "_decrypted")
        filename += "." + fileexten
        key_path = add_file("Select Key File Path")
        with open(key_path, "rb") as key_file:
            key = key_file.read()
            try:
                os.remove(key_path)
            except PermissionError:
                pass
        # choice = input("Do you want a new decrypted copy of the file or for the current copy to be decrypted?(New/Current)\n")
        # possible_inputs = ["New", "new", "Current", "current"]
        # while choice not in possible_inputs:
        #     print("Please enter a valid choice.")
        with open(filepath,"rb") as file:
            content = file.read()
        content_decrypted = Fernet(key).decrypt(content)
        # if choice == "New" or choice == "new":
        #     with open(filename,"wb") as file:
        #         file.write(content_decrypted)
        # else:
        with open(sav(), "wb") as file:
            file.write(content_decrypted)
        
    except FileNotFoundError:
        print("Please enter a valid file location.")
#encryption(input())
# decryption(input())