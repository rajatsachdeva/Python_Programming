#
# Working with JSON data
#

import urllib2
import json

# Function to print the json data in customized format
def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
    
    # Now we can access the contents of the JSON like any other Python Object
    if "title" in theJSON["metadata"]:
        print theJSON["metadata"]["title"]
    
    # output the number of events, plus the magnitude and each event name
    count = theJSON["metadata"]["count"]
    print str(count) + " event recorded"
    
    # For each event, print the place where it occurred
    for i in theJSON["features"]:
        print i["properties"]["place"]
        
    # Print only the events that only have a magnitude greater than 4
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print "mag = 2.1f, place = %s" % i["properties"]["mag"], i["properties"]["place"]
            
    # print only the events where at least 1 person reported feeling something
    print "Events that were felt:"
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if (feltReports != None) & (feltReports > 0):
            print "%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times"
        
def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
  
  # Open the URL and read the data
  webUrl = urllib2.urlopen(urlData)
  resultCode =  webUrl.getcode()
  if 200 == resultCode:
      data = webUrl.read()
      # print data
      # Print out our custmized Results
      printResults(data)
  else:
      print "Received an error from server, cannot retrieve results " + str(resultCode)
  print "\n---End Of Main---"

if __name__ == "__main__":
    main()