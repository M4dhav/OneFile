import shutil
from save import add_file
from save import sav
from save import ret_dir
from save import new


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
def ma():
    filename = add_file("Select File to be archived")
    newname= ret_dir()
    formatf=new()
    shutil.make_archive(newname,formatf,filename)
    

