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
from lxml import etree
from lxml.etree import tostring
#from lxml import etree
#from HTMLParser import HTMLParser


def parse_response(doc, system):
	results = []
	rescount = 0
	root = doc.getroot()
	if system == '-g':
		res = root.xpath("//h3[contains(@class,\"r\")]/a/@href")
	else:
		res = root.xpath("//a[contains(@class,\"link\")]/@href")
	for r in res:
#		re = etree.fromstring(tostring(r))
#		href = re.xpath("//a/@href")
#		print(tostring(href))
#		print(r)
		results.append(r)

		print(rescount, results[rescount])

		rescount += 1
	print(len(results))
def search(fstr, system):
	query = urllib.urlencode({'q': fstr})
	if system == '-g':
		url = 'https://www.google.com/search?q=' + query
	else:
		 url = 'http://www.yandex.ru/search/?query=' + query + '&lr=213&p=1'
	req = urllib2.Request(url, headers = {'User-Agent' : 'Firefox'})
	page = urlopen(req)
	if system == '-y':
		print(page.read())
	doc = parse(page)
	parse_response(doc, system)



if len(sys.argv) == 3:
	system = sys.argv[1]
	fstr = sys.argv[2]
	print("s:", system)
	print("fs:", fstr)
	search(fstr, system)


else:
	print("usage:\n./ topview.py [-g,-y] [search string]\n-g - google\n-y - yandex\n")
