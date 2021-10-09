import scrapy
from scrapy import item                             #add this
from downloadpics.items import DownloadpicsItem     #add this
from urllib.parse import urljoin                    #add this to use urljoin
from bs4 import BeautifulSoup
import requests




class GetpicsSpider(scrapy.Spider):
    name = 'getpics'
    #allowed_domains = ['getpics.com']
    #this project is to download the webs which belongs to one person,for example 'liuyaxi'
    #need to write codes to get the pic_web urls
   # urlname = 'liuxi'
    #name_url = 'https://meilulu.me/t/' + urlname + '/'
    #use another method to do this,scrapy shell
    #response.css('div.my-card>a::attr(href)').extract()
    #get a list to start_urls
    
    #url = ['/item/4638.html', '/item/4668.html', '/item/4704.html', '/item/4760.html', '/item/4839.html', '/item/4843.html', '/item/4862.html', '/item/4863.html', '/item/4869.html', '/item/4874.html', '/item/5634.html', '/item/5646.html', '/item/5767.html', '/item/5796.html', '/item/5825.html', '/item/6417.html', '/item/6438.html', '/item/6669.html']
    #url = ['/item/3204.html', '/item/4739.html', '/item/4744.html', '/item/4753.html', '/item/4754.html', '/item/4761.html', '/item/4763.html', '/item/4878.html', '/item/4939.html', '/item/5668.html', '/item/5669.html', '/item/5794.html', '/item/6430.html', '/item/6431.html', '/item/6437.html', '/item/7460.html', '/item/7485.html', '/item/7668.html', '/item/7701.html', '/item/7707.html', '/item/7709.html', '/item/8768.html', '/item/8887.html']
#
#    url_final = []
#    for a in url:
#        url_a = 'https://meitulu.me' + a
#        url_final.append(url_a)
    
    #use a function to do these things
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
            #print(aa.get('href'))
            bb = aa.get('href')
            cc =urljoin('https://meitulu.me' , bb)
            uu.append(cc)
        print(uu)
        return uu
    girlname = 'xiaopanshu'
    url_final = geturl('https://meitulu.me/t/' + girlname +'/')

    start_urls = url_final

    def parse(self, response):
        imageUrls = response.css('div.mb-4 img::attr(src)').extract()
        urllist = []
        for a in imageUrls:
            url_a = urljoin('https://meitulu.me',a)
            urllist.append(url_a)
            print(urllist)

        item = DownloadpicsItem()
        item['image_urls'] = urllist
        yield item

        nextPage = response.css('li.page-item a::attr(href)').extract()
        yield response.follow(nextPage[-1],callback=self.parse)
