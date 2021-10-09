import urllib.request
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin

def geturl(html):
    htmlcode = requests.get(html)
    #htmlcode.encoding = 'utf-8'
    htmlContent = htmlcode.text
    tree = BeautifulSoup(htmlContent,'html.parser')
    #print(tree)

    uu = []
    #for aa in tree.select('div.container pt-3'):
    a_list = tree.select('div.my-card a[href$="html"]')
    for aa in a_list:
        print(aa.get('href'))
        bb = aa.get('href')
        cc =urljoin('https://meitulu.me' , bb)
        uu.append(cc)
    print(uu)
    return uu
#name = 'yangxiaoqinger'
#name = 'Barbiekeer'
#geturl('https://meitulu.me/t/' + name +'/')

