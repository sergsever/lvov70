#!/usr/bin/env python
import sys
import urllib
#import urllib.request
#from urllib import urlopen
#import urllib.parse
#import http.cookiejar
import json
import requests
#from requests import urlopen
import lxml
import lxml.html
from lxml.html import parse
from lxml import etree
from bs4 import UnicodeDammit
from lxml.etree import tostring
import re
#pattern
from pattern.web import Google, plaintext
from pattern.web import SEARCH
import subprocess

#from lxml import etree
#from HTMLParser import HTMLParser


def parse_response(_results, system):
	results = {}
	rescount = 0

#	root = doc.getroot()
#	if system == '-g':
#		res = root.xpath("//h3[contains(@class,\"\")]/a/@href")
#	else:
#		res = root.xpath("//a[contains(@class,\"url\")]/@href[contains(\"url\")]/@url/@q")
	for r in _results:
		p = re.findall("http[s]?://[\w|\.]+", r.url)
		print("p:", p)
		addr = str(p)
		addr = addr[9:100]
		print("re:", addr)
		results[addr] = r
		print(rescount, results[addr])
		rescount += 1
	print(len(results))
	cmd = ['host', '-t', 'txt', results.keys()[3], 'dnsc1.m10.cair.ru']
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
			     stderr=subprocess.PIPE)
	out = p.communicate('foo\nfoofoo\n')
	print("out:", out)
def search(fstr, system):
	if system == '-g':
		url = 'https://www.google.com/search?q={}'
	else:
		url = "https://www.yandex.ru/search/?text={}"


#	url = url.format(urllib.request.pathname2url(fstr))
	print("url:", url)
#	if system == '-y':
#		req = urllib.request.Request(url, headers = {'User-Agent' : 'Mozilla', 'cookie' : '751d106e', 'Infohash' : '47b90cdddd1c5ad183e858d6df2a88ce89c83628', 'host' : 'ya.ru'})
#	else:
#		req = urllib.request.Request(url, headers = {'User-Agent' : 'Mozilla'})

	try:
#		page = urllib.request.urlopen(req, timeout = 10)
		engine = Google(license=None, language="en")
		results = engine.search(fstr, count=10,type=SEARCH)
		print("result:", results[0].text)
		if system == '-y':
			parser = etree.HTMLParser(encoding='windows-1251')
		else:
			 parser = etree.HTMLParser(encoding='utf-8')
#		doc = parse(results[0].download(timeout=10), parser)
#			print(doc)
		parse_response(results, system)
	except Exception as e:
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
