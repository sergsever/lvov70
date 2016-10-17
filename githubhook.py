#!/usr/bin/python
import cgi

print("Content-Type: text/html")
fs = cgi.FieldStorage()
with open("ghook.log", "a+") as log:
	for key in fs.keys():
	log.write(key, fs[key].value)
