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
off = 0

# Input Steam username and write full path to XML file

print ("""SteamID... 
Enter your game login on Steam:""")

name = input()

steamxml = "http://steamcommunity.com/id/{0}?xml=1".format(name)

# END Input Steam username and write full path to XML file

# Download XML User File

file_name = (name + ".xml")
u = urllib.request.urlopen(steamxml)
f = open(file_name, "wb")
meta = u.info()
fsize = int(meta.get("Content-Length"))

if fsize < 10000:

	off = 1
	print ("\nCheck Steam server availability!")

else:

	print ("\nDownloading system information. File Size: {0} Bytes".format(fsize))

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

try:

	xml = parse(file_name)
	getid = xml.getElementsByTagName("steamID64")

	for node in getid:

		SteamID64 = node.childNodes[0].nodeValue
		print ("\nSteamID64: ", SteamID64)

except xml.parsers.expat.ExpatError:

	print ("Error parse!")

# END XML Parser

# Get Api Key

if off == 0:

	f = open("api_key.txt","r")
	apikey = f.readline()
	secretapi = apikey [:4] + "*" * 28
	print ("APIKEY: ", secretapi)

else:

	print ("APIKEY: Parsing failed. First you need to get all settings!.. Try again")

# END Ger Api Key

# Download JSON File

steamjson = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={0}&steamids={1}".format(apikey, SteamID64)

file_name = (name + ".json")
u = urllib.request.urlopen(steamjson)
f = open(file_name, "wb")
meta = u.info()
fsize = int(meta.get("Content-Length"))

print ("\nDownloading JSON file. Size: {0} Bytes".format(fsize))

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

# END Download JSON File

# Exit

print ("\nPress key for exit...")
input()

# END Exit