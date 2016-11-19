#!/usr/bin/python

import urllib
import re


num = 3223
html = 'http://www.meitulu.com/item/%d.html'% num
n = 7
page = urllib.urlopen(html)
html_yuan = page.read()
reg = r'src=(http.+?\d{17}\.jpg)'
imgreg = re.compile(reg)
imglist = re.findall(imgreg,html_yuan)
print imglist
for img_false in imglist:
    urllib.urlretrieve(img_false,'girl%d.jpg'% n)
    n += 1
print n
m = n
for x in range(2,17):
    html ='http://www.meitulu.com/item/%d_%s.html'%(num,x)
    print html
    page = urllib.urlopen(html)
    html_yuan = page.read()
    reg = r'src=(http.+?\d{17}\.jpg)'
    imgreg = re.compile(reg)
    imglist = re.findall(imgreg,html_yuan)
    print imglist
    for img_false in imglist:
        urllib.urlretrieve(img_false,'girl%d.jpg'% m)
        m += 1
print m

