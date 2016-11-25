#!/usr/bin/python

import urllib
import re
import os 


num = 8615
html = 'http://www.meitulu.com/item/%d.html'% num
n = 1
page = urllib.urlopen(html)
html_yuan = page.read()
reg = r'src=(http.+?\d{17}\.jpg)'
imgreg = re.compile(reg)
imglist = re.findall(imgreg,html_yuan)
print imglist

os.mknod('list')
for img_url in imglist:
    #f= open('/home/wolf/pictest/list','a')
    #f.write(img_url+'\n')
    with open('/home/wolf/pictest/list','a') as f:
        f.write(img_url+'\n')
        n = n + 1
    f.close()

#n += 1
#print n

m = n
for x in range(2,15):
    html ='http://www.meitulu.com/item/%d_%s.html'%(num,x)
    print html
    page = urllib.urlopen(html)
    html_yuan = page.read()
    reg = r'src=(http.+?\d{17}\.jpg)'
    imgreg = re.compile(reg)
    imglist = re.findall(imgreg,html_yuan)
    print imglist
    for img_url in imglist:
        with open('/home/wolf/pictest/list','a') as e:
            e.write(img_url+'\n')
            m = m + 1
        e.close()
print m
os.system('aria2c -i list')
os.remove('list')
