#!/usr/bin/python3

# for loops
# Here line is an iterator

# read the lines from the file
fh = open('lines.txt')
for line in fh.readlines():
    print(line, end="")

# this end="" in print allows to avoid the implicit newline
# In python 2 ';' is used at the end of statement to get the same
# behavior

# close the file
fh.close()