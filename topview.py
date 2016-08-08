#!/usr/bin/env python
import sys
import urllib
import urllib2
from urllib2 import urlopen
#import urllib.parse
import json
import requests
#from requests import urlopen
import lxml
import lxml.html
from lxml.html import parse
from lxml.etree import tostring
#from lxml import etree
#from HTMLParser import HTMLParser

def parse_response(doc):
	root = doc.getroot()
	res = root.xpath("//h3[contains(@class,\"r\")]")
	print(tostring(res[1]))

def gsearch(fstr):
	query = urllib.urlencode({'q': fstr})
	url = 'https://www.google.com/search?q=' + query
	req = urllib2.Request(url, headers = {'User-Agent' : 'Firefox'})
	page = urlopen(req)
	doc = parse(page)
	parse_response(doc)

if len(sys.argv) == 3:
	system = sys.argv[1]
	fstr = sys.argv[2]
	print("s:", system)
	print("fs:", fstr)
	if system == '-g':
		gsearch(fstr)

else:
	print("usage:\n./ topview.py [-g,-y] [search string]\n-g - google\n-y - yandex\n")