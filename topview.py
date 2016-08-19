#!/usr/bin/env python
import sys
import urllib2
import requests
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

class Result:
	def __init__(self,url, res, categories):
		self.url = url
		self.res = res
		self.categories = categories
	def set_categories(self, _categories):
		self.categories = _categories
	def get_url(self):
		return self.url

def get_resources(category):
	url = 'https://netpolice-info-data-aggregation-v1.p.mashape.com'
	headers = {u"X-Mashape-Key" : u"Key"}
	data = {u"user_id" : u"id"}
#	req = requests.Request('GET',url, data='user_id=1')
#	req = urllib2.request.Request(url, headers = {'User-Agent' : 'Mozilla', 'cookie' : '751d106e', 'Infohash' : '47b90cdddd1c5ad183e858d6df2a88ce89c83628', 'host' : 'ya.ru'})
	resp = requests.get(url, headers=headers, data=data)
	print("resp:", resp.text)

def find_categories(results):
	categories = []
	for key in results.keys():
		categories = []
		result = results[key]
		cmd = ['host', '-ttxt', result.get_url(), 'dnsc1.m10.cair.ru']
		p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
			     stderr=subprocess.PIPE)
		out = str(p.communicate('foo\nfoofoo\n'))
		print(out)
		cats = re.findall("[\d|\,]+", out)
		if len(cats) >= 7:
			strs = cats[7].split(',')
			for s in strs:
				categories.append(int(s))

		result.set_categories(categories)
		print("cats:", categories)

def parse_response(_results, system):
	results = {}
	rescount = 0
	
#	root = doc.getroot()
#	if system == '-g':
#		res = root.xpath("//h3[contains(@class,\"\")]/a/@href")
#	else:
#		res = root.xpath("//a[contains(@class,\"url\")]/@href[contains(\"url\")]/@url/@q")
	for r in _results:
		p = re.findall("http[s]://?[\w|\.]+", r.url)
		print("p:", p)
		addr = str(p)
		addr = addr[9:100]
		print("re:", addr)
		result = Result(url=addr, res=r, categories=[])
		results[addr] = result
		print(rescount, results[addr])
		rescount += 1
	print(len(results))
	get_resources(category=64)
	tres = {'www.specialist.ru' : 'test'}
#	find_categories(results)

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
