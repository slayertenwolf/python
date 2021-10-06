import scrapy
from get5avv.items import Get5AvvItem
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class Get5aavSpider(scrapy.Spider):
    name = 'get5aav'
    # allowed_domains = ['5aav.com']
    urlList = []
    numUrl = [1926]
    for x in numUrl:
        # y = 'https://www.5aav.com/xgmv/%d.html' % x
        y = 'http://www.lulu78.net/sexgirl/%d.html' % x
        urlList.append(y)
    start_urls = urlList

    # aUrl = 'https://www.5aav.com/xgmv/list_1_9.html'
    # getUrl = requests.get(aUrl)
    # getUrl.encoding = 'utf-8'
    # getUrlContent = getUrl.content
    # bs4Url = BeautifulSoup(getUrlContent,'lxml')
    # pagesList = []
    # for z in  bs4Url.select('.postlist ul li a'):
    #     pageUrl = urljoin('https://www.5aav.com',z.get('href'))
    #     pagesList.append(pageUrl)
    # start_urls = pagesList
    # print(start_urls)

    def parse(self, response):
        # imgUrls = response.css('div.main-image p img::attr(src)').getall()
        imgUrls = response.css('div.imgbox a img::attr(data-original)').getall()
        item = Get5AvvItem()
        item['image_urls'] = imgUrls
        yield item

        # nextPageUrl = response.css('div.pagenavi li a::attr(href)').getall()
        nextPageUrl = response.css('div.pages a::attr(href)').getall()
        yield response.follow(nextPageUrl[-1],callback=self.parse)

