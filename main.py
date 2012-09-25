#!usr/bin/env python3
# File: main.py
# Main File

import os
import sys
import urllib
import pymongo

from xml.dom.minidom import *

name = ""
steamxml = ""
steamjson = ""

# Input Steam username and write full path to XML file

print ("SteamID...")
print ("Enter your game login on Steam: ")
name = input()
steamxml = "http://steamcommunity.com/id/" + name +"?xml=1"
print (steamxml)
input()

# END Input Steam username and write full path to XML file