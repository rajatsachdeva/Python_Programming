#
# fetch internet data such as JSON, HTML, XML
# We can work with this data easily
#

import urllib2

def main():
    # Open a connection to a URL using urllib2
    webUrl = urllib2.urlopen("http://joemarini.com")  
    
    # get the result code and print it
    print "result code: " + str(webUrl.getcode())
    
    # Read the data from the URL and print it
    data = webUrl.read()
    print data  

if __name__ == "__main__":
    main()