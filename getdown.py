#!/usr/bin/python

import urllib
import re

n = 1
for m in range(2,17):
    html ='http://www.meitulu.com/item/5418_%s.html'% m
    print html
    page = urllib.urlopen(html)
    html_yuan = page.read()
    reg = r'src=(http.+?20150614\d{9}\.jpg)'
    imgreg = re.compile(reg)
    imglist = re.findall(imgreg,html_yuan)
    print imglist
    for img_false in imglist:
  #  img_true = img_false.replace('\\','')
  #  print img_true
        urllib.urlretrieve(img_false,'girl%d.jpg'% n)
        n += 1
print n
