#! /usr/bin/python

import urllib2

request = urllib2.Request("http://www.liaoxue.com")
response = urllib2.urlopen(request)
print response.read()
