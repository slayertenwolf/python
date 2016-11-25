#!/usr/bin/env python
# coding=utf-8

import re
import os
import urllib


num = 7064 
html = 'http://www.meitulu.com/item/%d.html'% num
n = 1
page = urllib.urlopen(html)
html_code = page.read()
reg = r'src=(http.+?\d{17}\.jpg)'
imgreg = re.compile(reg)
imglist = re.findall(imgreg,html_code)
print imglist

getdir = os.getcwd()
os.mknod('list')
dir_name = getdir+'/list'
for img_url in imglist:
    with open(dir_name,'a') as file:
        file.write(img_url+'\n')
        n = n + 1
    file.close()

for x in range(2,17):
    html = 'http://www.meitulu.com/item/%d_%s.html'%(num,x)
    print html
    page = urllib.urlopen(html)
    html_code = page.read()
    reg = r'src=(http.+?\d{17}\.jpg)'
    imgreg = re.compile(reg)
    imglist = re.findall(imgreg,html_code)
    print imglist
    for img_url in imglist:
        with open(dir_name,'a') as file:
            file.write(img_url+'\n')
            n = n + 1
        file.close()
print n
os.system('aria2c -i list')
os.remove('list')

