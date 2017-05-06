#
# Using System Shell Methods
#

import os 
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile

def main():
    # Make a duplicate of an existing file
    if path.exists("textfile.txt"):
        # get the path to the file in current directory
        src = path.realpath("textfile.txt")
        
        # Separate the path from the file name
        pathname, filename = path.split(src)
        
        print "path: " + pathname
        print "file: " + filename
        
        # let's make a backup copy by appending "bak" to the name
        dst  = src + ".bak"
        
        # Now use the shell to make a copy of the file
        # copy fucntion only copies the file data 
        shutil.copy(src, dst)
        
        # Now to copy information such as permissions, modification times, and others
        # Use copystat
        shutil.copystat(src,dst)
        
        # rename the orignal file name 
        #os.rename("textfile2.txt", "newfile.txt")
        
        # Now put things in a ZIP archive
        root_dir, tail = path.split(src)
        #make_archive("Name of the archive", "format of archive"
        #shutil.make_archive("archive", "zip", root_dir)
        
        # more fine-grained control over ZIP Files
        with ZipFile("testzip.zip", "w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("textfile.txt.bak")
                
if __name__ == "__main__":
    main()