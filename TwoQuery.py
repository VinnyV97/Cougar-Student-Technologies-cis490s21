import os
import re
import urllib.request
import json

directory = r"C:\Users\Vinny\Documents\CIS 490\prototype\streets" # set to own directory
API_key = "&key=" + "AIzaSyD6XYTJYrV1g9BZLiTLnwAkFgpASFg_MJY" # set to own key
size = "300x300" 

# requesting metadata before image
def GetMeta(address, directory):
  base = "https://maps.googleapis.com/maps/api/streetview/metadata?"
  location = "&location=" + address
  url = base + location + API_key
  file = address + ".json"
  urllib.request.urlretrieve(url, os.path.join(directory, file)) #saves metadata as .json file into directory

  """
  if file.status.OK
    print("GetStreet(address, directory)"
  else
    print("No image per request")
  """

# image request
def GetStreet(address, directory):
  base = "https://maps.googleapis.com/maps/api/streetview?size=" + size
  location = "&location=" + address 
  heading = "&heading=0" #north direction
  file = address + "_A1.jpg"
  url = base + location + heading + API_key
  urllib.request.urlretrieve(url, os.path.join(directory, file))

  heading = "&heading=90" #east direction
  file = address + "_A2.jpg"
  url = base + location + heading + API_key
  urllib.request.urlretrieve(url, os.path.join(directory, file))

  heading = "&heading=180"
  file = address + "_A3.jpg" #south direction
  url = base + location + heading + API_key
  urllib.request.urlretrieve(url, os.path.join(directory, file))

  heading = "&heading=270" #west direction
  file = address + "_A4.jpg" 
  url = base + location + heading + API_key
  urllib.request.urlretrieve(url, os.path.join(directory, file))


address = input("Please type an address or coordinate to query: ")
address = address.replace(" ", "") #removes whitespace in input

GetMeta(address, directory) #run for metadata first

GetStreet(address, directory) #run if you just want the images

#for running with OSMnx
#for i in route
  #GetPic(route[i], directory)