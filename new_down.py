#!/usr/bin/python

import re
import urllib

def getSource(html):
    source = urllib.urlopen(html)
    html_source = source.read()
    return html_source

def findimg(yuan,n):
    reg = r'lazysrc=\s*(http://www.+?\.jpg)'
    re_reg = re.compile(reg)
    imglist = re.findall(re_reg,yuan)
    print imglist
    for m in imglist:
        urllib.urlretrieve(m,'%s.jpg'% n)
    print n
   
Ran = range(2,10)
#RRan = range(10,100)
n =246

for b in Ran:
    html ='http://www.mm4493.com/meitu/46714_%s.html'% b
    print html
    yuan = getSource(html)
    findimg(yuan,n)
    n += 1
