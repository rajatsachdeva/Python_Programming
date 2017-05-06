#!/usr/bin/python3
# Exception Handling

try:
    fh = open('xlines.txt')
    for line in fh.readlines():
        print(line)
except IOError as e:
    print ("Error while opening the file: ({})".format(e))

print ("after badness")