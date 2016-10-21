#!/usr/bin/python
#coding=utf-8

import urllib
import re

def getHtml_first(url_first):
    page_first = urllib.urlopen(url_first)
    html_first = page_first.read()
    return html_first
    print html_first

def findurl(html_first):
    reg = r'(http://dp.pconline.com.cn/public/pyhoto/.+\d{7})">'
    urlreg = re.compile(reg)
    urllist = re.findall(urlreg,html_first)
    return urllist[0]
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 5
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg'% x)
        x = x + 1
    print imglist

url_first= "http://dp.pconline.com.cn/photo/3669965_2.html"
print url_first
a = getHtml_first(url_first)
url = findurl(a)
print url


html = getHtml(url)

getImg(html)
