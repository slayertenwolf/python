#!/usr/bin/python

import urllib
import re
import os

os.chdir('../')
os.mkdir('meitulugirls2')
os.chdir('./meitulugirls2')

print os.getcwd()
n = 1
for m in range(2,15):
    html ='http://www.meitulu.com/item/8039_%s.html'% m
    print html
    page = urllib.urlopen(html)
    html_yuan = page.read()
    reg = r'src=(http.+?/\d{17}\.jpg)'
    imgreg = re.compile(reg)
    imglist = re.findall(imgreg,html_yuan)
    print imglist
    for img_false in imglist:
  #  img_true = img_false.replace('\\','')
  #  print img_true
        urllib.urlretrieve(img_false,'girl%d.jpg'% n)
        n += 1
print n
