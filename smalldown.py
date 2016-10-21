#! /usr/bin/python

import urllib
import re

html = 'http://desk.zol.com.cn/bizhi/2086_26587_2.html'
page = urllib.urlopen(html)
yuan = page.read()

num = 1032
reg = r'href="(/showpic/1920x1080.+?\.html)"'
rereg = re.compile(reg)
urllist = re.findall(rereg,yuan)
for x in urllist:
    y = 'http://desk.zol.com.cn'+ x
    print y
    page2 = urllib.urlopen(y)
    yuan2 = page2.read()
    reg2 = r'src="(.+\.jpg)"'
    rereg2 = re.compile(reg2)
    urllist2 = re.findall(rereg2,yuan2)
    print urllist2
    for z in urllist2:
        urllib.urlretrieve(z,'girl%s.jpg'% num)










urllib.urlretrieve(html,'116.jpg')
