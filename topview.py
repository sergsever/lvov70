#!/usr/bin/env python3
import sys
import urllib
import urllib.request
#from urllib import urlopen
#import urllib.parse
import http.cookiejar
import json
import requests
#from requests import urlopen
import lxml
import lxml.html
from lxml.html import parse
from lxml import etree
from bs4 import UnicodeDammit
from lxml.etree import tostring
#from lxml import etree
#from HTMLParser import HTMLParser


def parse_response(doc, system):
	results = []
	rescount = 0

	root = doc.getroot()
	if system == '-g':
		res = root.xpath("//h3[contains(@class,\"\")]/a/@href")
	else:
		res = root.xpath("//a[contains(@class,\"url\")]/@href")
	for r in res:
		results.append(r)
		print(rescount, results[rescount])
		rescount += 1
	print(len(results))
def search(fstr, system):
	if system == '-g':
		url = 'https://www.google.com/search?q={}'
	else:
		url = "https://www.yandex.ru/search/?text={}"


	url = url.format(urllib.request.pathname2url(fstr))
	print("url:", url)
	if system == '-y':
		req = urllib.request.Request(url, headers = {'User-Agent' : 'Mozilla', 'cookie' : '751d106e', 'Infohash' : '47b90cdddd1c5ad183e858d6df2a88ce89c83628', 'host' : 'ya.ru'})
	else:
		req = urllib.request.Request(url, headers = {'User-Agent' : 'Mozilla'})
	try:
		page = urllib.request.urlopen(req, timeout = 10)
		if system == '-y':
			parser = etree.HTMLParser(encoding='windows-1251')
		else:
			 parser = etree.HTMLParser(encoding='utf-8')
		doc = parse(page, parser)
#			print(doc)
		parse_response(doc, system)
	except urllib.error.URLError as e:
		print(e)
#	if system == '-y':

#	print(doc)



if len(sys.argv) == 3:
	system = sys.argv[1]
	fstr = sys.argv[2]
	print("s:", system)
	print("fs:", fstr)
	search(fstr, system)


else:
	print("usage:\n./ topview.py [-g,-y] [search string]\n-g - google\n-y - yandex\n")
