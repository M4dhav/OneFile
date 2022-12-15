import os
from cryptography.fernet import Fernet
from save import sav
from save import add_file

def encryption(filepath):
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
    key_path = sav("Choose Key File Path (Please save as '.key' file)")
    # try:
    #     open(key_path, "r")
    # except FileNotFoundError:
    #     print("Please select a valid key location.")
    #     key_path = sav("Choose Key File Path (Please save as '.key' file)")
    with open(key_path, "wb") as key_file:
        key_file.write(key)
    with open(filepath,"rb") as file:
        content = file.read()
    content_encrypted = Fernet(key).encrypt(content)
    save_file_path = sav("Select Encrypted File Path")

    with open(save_file_path, "wb") as file:
        file.write(content_encrypted)
    # else:
    #     with open(filepath, "wb") as file:
    #         file.write(content_encrypted)
    #     return
    

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