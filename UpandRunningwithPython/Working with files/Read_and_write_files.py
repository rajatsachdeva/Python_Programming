#
# Read and Write Files
#

# There is no need to import any class for file read or write 
# as these are available by default in python

def main():
    # Open a file for writing and create it if it doesn't exist
    f1 = open("textfile.txt", "w+") # Actually opened in read/write mode
    
    # Open a file in append mode, it's create a file if it doesn't exist 
    # and add the data at end of the file 
    f2 = open("textfile2.txt", "a+")
    # Write in the file
    for i in range(10):
        f1.write("This is line #%d\n" %(i + 1))
        #f2.write("This is line #%d\n" %(i + 1))

    # Close the file when done
    f1.close()
    f2.close()
    
    # Open the file back up and read the contents
    f = open("textfile.txt","r")
    if f.mode == 'r': # check to make sure that the file was opened
    # use the read() function to read the entire file
        contents = f.read()
        print contents
    
    f.close()
    f = open("textfile.txt","r")
    fl = f.readlines() # readlines reads the individual lines into a list
    for x in fl:
      print x

if __name__ == "__main__":
    main() 