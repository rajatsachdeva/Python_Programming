#!/usr/bin/python3

# http://docs.python.org/py3k/library/index.html

# Using standard library modules

import sys

def main():
    print('Python version {}.{}.{}'.format(*sys.version_info))
    print(sys.platform)
    
    # selective import
    import os
    # name of OS
    print(os.name)
    # Environment Variable
    print(os.getenv('PATH'))
    # current working directory
    print(os.getcwd())
    # string of random bytes
    print(os.urandom(25))
    
    import urllib.request
    # open a web page
    page = urllib.request.urlopen('http://joemarini.com')
    # page is an iterable object
    print(page)
    for line in page: print(str(line,encoding = 'utf_8'), end ='')
    
    import random
    print(random.randint(1, 1000))
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)
    
    import datetime
    now = datetime.datetime.now()
    print (now)
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)
    
if __name__ == "__main__": main()
