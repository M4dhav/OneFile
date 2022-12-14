import shutil
import os
'''LIST OF FUNCTIONS:
1. copyD:-copies files to another directory
2. copyF:-copies files to another file
3. copyT:-copies entire tree to destinaton(destination folder must not exist already)
4. delT:-deletes entire tree of files from specified dest
5. FS:-Searches for the directory of the python file
'''
def copyD():
    '''COPY FILES TO ANOTHER DIRECTORY'''
    source = input("Enter the source path of the file: ")
    destination = input("Enter the directory where the file needs to be: ")

    # Copy the content of   
    # source to destination
    dest = shutil.copy(source, destination)

    # Print path of newly
    # created file
    print("the file is stored at: ", dest)
def copyF():
    '''COPY FILES FROM ONE FILE TO ANOTHER'''

    # Source path
    source = input("Enter the source path of the file: ")
    # Destination path
    destination = input("Enter the path of the other file: ")

    dest = shutil.copyfile(source, destination)

    print("Destination path:", dest)
def copyT():
    '''COPY ENTIRE TREE FROM SOURCE TO DEST,DEST MUST NOT EXIST FROM BEFORE'''
    # path
    path = input("Enter the path of the file:")

    print("Before copying file:")
    print(os.listdir(path))

    # Source path
    src = path

    # Destination path
    dest = path+'/dest'

    # Copy the content of
    # source to destination
    destination = shutil.copytree(src, dest)

    print("After copying file:")
    print(os.listdir(path))

    # Print path of newly
    # created file
    print("Destination path:", destination)
def delT():
    '''DELETE ENTIRE DIRECTORY TREE'''
    # location
    location = input("Enter the path to the directory")

    # directory
    dir = input("Enter the directory you want to delete")

    # path
    path = os.path.join(location, dir)

    # removing directory
    shutil.rmtree(path)
def FS():
    '''SEARCH FOR A FILE'''
    # file search
    cmd = input("Enter the name of the file whose path you want to find: ")

    # Using shutil.which() method
    locate = shutil.which(cmd)

    # Print result
    print(locate)
