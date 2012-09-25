#!usr/bin/env python3
# File: main.py
# Main File

import os
import sys
import urllib.request

from xml.dom.minidom import *

name = ""
steamxml = ""
steamjson = ""

# Input Steam username and write full path to XML file

print ("SteamID...")
print ("Enter your game login on Steam: ")
name = input()
steamxml = "http://steamcommunity.com/id/" + name +"?xml=1"

# END Input Steam username and write full path to XML file

# Download XML User File

file_name = (name + ".xml")
u = urllib.request.urlopen(steamxml)
f = open(file_name, "wb")
meta = u.info()
fsize = int(meta.get("Content-Length"))
print ("Downloading system information. File Size: %s Bytes" % (fsize))

fsize_dl = 0
block_sz = 8192

while True:

	buffer = u.read(block_sz)
	
	if not buffer:
		
		break

	fsize_dl += len(buffer)
	f.write(buffer)
	status = r"%10d [%3.2f%%]" % (fsize_dl, fsize_dl * 100. / fsize)
	status = status + chr(8)*(len(status)+1)
	print (status)

f.close()

# END Download XML User File

# XML Parser

xml = parse(file_name)
getid = xml.getElementsByTagName("steamID64")

for node in getid:

	SteamID64 = node.childNodes[0].nodeValue

# END XML Parser