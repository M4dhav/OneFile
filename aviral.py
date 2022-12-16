import shutil
from save import add_file
from save import sav
from save import ret_dir

'''COMPRESSION FUNCTIONS'''
def uz():
    # Full path of
    # the archive file
    filename = add_file("Select File to be unarchived")

    # Target directory
    extract_dir = ret_dir()

    # Format of archive file
    archive_format = input("Enter file format of zipped file")

    # Unpack the archive file
    shutil.unpack_archive(filename, extract_dir, archive_format)
    print("Archive file unpacked successfully.")
def ma():
    filename = add_file("Select File to be archived")
    newname= ret_dir()
    formatf=input("Enter the file format you want to zip the file in")
    shutil.make_archive(newname,formatf,filename)
    

