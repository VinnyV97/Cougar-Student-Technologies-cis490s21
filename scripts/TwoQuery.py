import os
import re
import urllib.request
import json
import requests

directory = r"C:\Users\Vinny\Documents\CIS 490\prototype\streets" # set to own directory
API_key = "&key=" + "AIzaSyD6XYTJYrV1g9BZLiTLnwAkFgpASFg_MJY" # set to own key
size = "640x640" # 640x640 is max 

# called first to request metadata and check if images are available
def GetMeta(address, directory):
  base = "https://maps.googleapis.com/maps/api/streetview/metadata?"
  location = "&location=" + address
  url = base + location + API_key
  file = address + ".json" #formats .json file to be saved 
  meta = requests.get(url) #requests metadata from GSV API
  meta_info = meta.json()  
  meta_status = meta_info['status'] 
  if meta_status == 'OK' : 
    print("Request found")
    print(meta_info)
    
    with open(os.path.join(directory, file), 'w') as f: #saves metadata into file in directory
      json.dump(meta_info, f)  

    GetStreet(address, directory) #requests images 

  else :
    print("Request cannot be made")
    print(meta_info)

# ran only if status == ok 
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

#GetStreet(address, directory) #run if you just want the images

#for running with OSMnx
#for i in route
  #GetMeta(route[i], directory)