#!/usr/bin/python

import re
import urllib

def getSource(html):
    source = urllib.urlopen(html)
    html_source = source.read()
    return html_source

def findimg(yuan,n):
    reg = r'src=(.+?/\d{17}\.jpg)'
    re_reg = re.compile(reg)
    imglist = re.findall(re_reg,yuan)
    print imglist
    for m in imglist:
        urllib.urlretrieve(m,'%s.jpg'% n)
        n += 1
    print n
   
Ran = range(2,13)
RRan = range(70,76)
n = 430

for a in RRan:
    for b in Ran:
        html ='http://www.meitulu.com/item/80%s_%s.html'% (a, b)
        print html
        yuan = getSource(html)
        findimg(yuan,n)
        n += 4 
