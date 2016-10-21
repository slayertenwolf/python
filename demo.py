#!/usr/bin/python

import urllib
import re
"""
html = "http://dp.pconline.com.cn/photo/3669965_2.html"
reg = r'href="(http://dp.pconline.com.cn/public/photo/)'
urlreg = re.compile(reg)
urllist = re.findall(urlreg,html)
print urllist
"""

def findurl(url_1):
    page1 = urllib.urlopen(url_1)
    html_yuan1 = page1.read()
    reg1 = r'href="(http://dp.pconline.+photoId=\d{7})"'
    reg1_re = re.compile(reg1)
    htmllist1 = re.findall(reg1_re,html_yuan1)
    print htmllist1
    return htmllist1 

def findimg(htmllist):
    for url_2 in htmllist1:
        page2 = urllib.urlopen(url_2)
        html_yuan2 = page2.read()
        reg2 = r'src="(.+\d+\.jpg)"'
        reg2_re = re.compile(reg2)
        htmllist2 = re.findall(reg2_re,html_yuan2)
        print htmllist2
        return htmllist2
def getimg(imglist,n):
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'girl%d.jpg'% n)


html = "http://dp.pconline.com.cn/photo/3672737.html"
htmllist1 = findurl(html)
imglist = findimg(htmllist1)
getimg(imglist,19)
