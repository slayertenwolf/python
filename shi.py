#!/usr/bin/python

import re
import urllib

html = "http://www.mzitu.com/73189/"
page = urllib.urlopen(html)
html_yuan = page.read()
print html_yuan
"""reg = r'src="(.+?\.jpg)"'
imgreg = re.compile(reg)
imglist = re.findall(imgreg,html_yuan)
print imglist
for img_url in imglist:
    urllib.urlretrieve(img_url,'111.jpg')
    """
