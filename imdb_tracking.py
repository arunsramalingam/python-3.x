#!/usr/bin/env python27

#Importing the modules

# from BeautifulSoup import BeautifulSoup
import sys
import urllib
from urllib.request import *
import re
import json

#Ask for movie title
title = input("Please enter a movie title: ")

#Ask for which year
year = input("which year? ")

#Search for spaces in the title string
raw_string = re.compile(r' ')

#Replace spaces with a plus sign
searchstring = raw_string.sub('+', title)

#Prints the search string
print (searchstring)

#The actual query
url = "http://www.imdbapi.com/?t=" + searchstring + "&y="+year

request = Request(url)

response = json.load(urlopen(request))

print (json.dumps(response,indent=2))