# 
# Python provides utilities to find if a path is file or directory 
# whether a file exists or not 
#

# Import OS module
import os
from os import path
from datetime import date, time , datetime
import time

def main():
    # print the name of os
    print "Os name is " + os.name
    
    # Check for item existence and type
    print "Item Exists: " + str(path.exists("textfile.txt"))
    print "Item is a file: " + str(path.isfile("textfile.txt"))
    print "Item is a directory: " + str(path.isdir("textfile.txt"))
    
    # Work with file paths
    print "Item's path: " + str(path.realpath("textfile.txt"))
    print "Item's path and name: " + str(path.split(path.realpath("textfile.txt")))
    
    # Get the modification time of the file
    t = time.ctime(path.getmtime("textfile.txt"))
    print "Modification time for 'textfile.txt' is : " + t
    
    print datetime.fromtimestamp(path.getmtime("textfile.txt"))
    
    # Calculate how long ago the file was modified
    td  = datetime.now() - datetime.fromtimestamp(path.getmtime("textfile.txt"))
    print "It has been " + str(td) + " since the file was updated"
    print "Or, " + str(td.total_seconds()) + " seconds"
    
if __name__ == "__main__":
    main()

    
    