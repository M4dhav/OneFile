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
    source = "path/main.py"
    destination ="path/main2.py"

    # Copy the content of
    # source to destination
    dest = shutil.copy(source, destination)

    # Print path of newly
    # created file
    print("the file is stored at: ", dest)
def copyF():
    '''COPY FILES FROM ONE FILE TO ANOTHER'''

    # Source path
    source = "csv/main.py"

    # Destination path
    destination = "csv/gfg/main_2.py"

    dest = shutil.copyfile(source, destination)

    print("Destination path:", dest)
def copyT():
    '''COPY ENTIRE TREE FROM SOURCE TO DEST,DEST MUST NOT EXIST FROM BEFORE'''
    # path
    path = 'C:/Users/ksaty/csv/gfg'

    print("Before copying file:")
    print(os.listdir(path))

    # Source path
    src = 'C:/Users/ksaty/csv/gfg'

    # Destination path
    dest = 'C:/Users/ksaty/csv/gfg/dest'

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
    location = "csv/gfg/"

    # directory
    dir = "dest"

    # path
    path = os.path.join(location, dir)

    # removing directory
    shutil.rmtree(path)
def FS():
    '''SEARCH FOR A FILE'''
    # file search
    cmd = 'anaconda'

    # Using shutil.which() method
    locate = shutil.which(cmd)

    # Print result
    print(locate)
