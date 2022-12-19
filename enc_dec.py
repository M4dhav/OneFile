import os
from cryptography.fernet import Fernet
from repetitive import sav
from repetitive import add_file

def encryption(filepath):
    try:
        open(filepath, "r")
    except FileNotFoundError:
        return
    key = Fernet.generate_key()
    key_path = sav("Choose Key File Path (Please save as '.key' file)")
    try:
        with open(key_path, "wb") as key_file:
            key_file.write(key)
    except FileNotFoundError:
        return
    with open(filepath,"rb") as file:
        content = file.read()
    content_encrypted = Fernet(key).encrypt(content)
    save_file_path = sav("Select Encrypted File Path")
    with open(save_file_path, "wb") as file:
        file.write(content_encrypted)
    

def decryption(filepath):
    try:
        open(filepath, "r")
    except FileNotFoundError:
        return
    key_path = add_file("Select Key File Path")
    try:
        with open(key_path, "rb") as key_file:
            key = key_file.read()
    except:
        return
    with open(filepath,"rb") as file:
        content = file.read()
    content_decrypted = Fernet(key).decrypt(content)
    save_file_path = sav("Select Decrypted File Path")
    with open(save_file_path, "wb") as file:
            file.write(content_decrypted)