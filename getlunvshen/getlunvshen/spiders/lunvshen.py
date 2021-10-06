import scrapy
from getlunvshen.items import GetlunvshenItem
from urllib.parse import urljoin
import urllib.request
from bs4 import BeautifulSoup
import requests

class LunvshenSpider(scrapy.Spider):
    name = 'lunvshen'
    # allowed_domains = ['lunvshen.org']
    # start_urls = ['https://www.lunvshen.org/t-978',]
    # start_urls = ['http://www.lulu78.net/sexgirl/1223.html']
    #//div[@class="topic-content"]/p/a/@href
    htmlcode = requests.get('https://www.lunvshen.org/tag-157')
    htmlcode.encoding = 'utf-8'
    htmlContent = htmlcode.text
    tree = BeautifulSoup(htmlContent,'lxml')
    # print(tree)
    uu = []
    for aa in tree.select('.item-content h1 a'):
        b = aa.get('href')
        c = urljoin('https://www.lunvshen.org/',b)
        uu.append(c)
    
    start_urls = uu
    print(start_urls)

    def parse(self, response):
        imageUrls = response.css('div.topic-content p img::attr(data-original)').getall()    
        # imageUrls = response.css('div.imgbox a img::attr(data-original)').getall()
        print(imageUrls)  
        item = GetlunvshenItem()
        item['image_urls'] = imageUrls
        yield item

        nextPage = response.css('div.prev-next a::attr(href)').get()
        yield response.follow(nextPage,callback = self.parse)

