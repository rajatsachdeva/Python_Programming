#!/usr/bin/python3

# Operating on character data with bytes and byte arrays
# bytes and bytearray are like tuples and lists except instead 
# of containing arbitary objects, bytes and bytearrays contains bytes.
# 8-bit word of data can hold up to 256(2^8) different values.

# In particular, it's convenient for converting strings 
# Bytearray is mutable list of bytes
# it doesn't hold any other kind of object but bytes

# bytes are immutable arrays of bytes

def main():  
    # Open the file in read mode with encoding as utf_8 
    fin = open("utf8.txt", 'r', encoding = 'utf_8')
    fout = open("utf8.html", 'w')
    
    outbytes = bytearray()
    for line in fin:
        for c in line:
            # Gives the integral equvivalent of that character
            # There are 128 values in UTF-8 that are just normal ASCII 
            # and they are 0 through 127
            # So greater than that will give something special
            if ord(c) > 127:
                                # an XML entity
                outbytes += bytes('&#{:04d};'.format(ord(c)), encoding = 'utf_8')
            else: 
                outbytes.append(ord(c))
    
    outstr = str(outbytes, encoding = 'utf_8')
    print(outstr, file = fout)
    print(outstr)
    print('Done')
        
if __name__ == "__main__": main()
