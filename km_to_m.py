#!/usr/bin/env python
from urllib.request import urlopen
import re
website = urlopen("http://www.google.com/")
html=website.read()
# links = re.findall('"((http|ftp)s?://.*?)"', website)
print(html)
kmh = int(input("Enter km/h: "))
mph =  0.6214 * kmh
print ("Speed:", kmh, "KM/H = ", mph, "MPH")