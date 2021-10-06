import scrapy
from mypic.items import MypicItem
import re

class GetpicSpider(scrapy.Spider):
    name = 'getpic'
    # allowed_domains = ['meitulu.com']
    # c=[]
    # for x in [8808]:
    #     y = 'http://meitulu.92demo.com/item/%d.html' % x
    #     c.append(y)
    # start_urls = c
    start_urls= ['http://meitulu.92demo.com/t/yejiayi/']

    def parse(self, response):
        imgUrls=response.xpath('//center/a/img/@src').getall()
        # imgUrls = response.css('div.content').getall()
        # print(type(imgUrls),imgUrls)
        item = MypicItem()
        item['image_urls'] = imgUrls
        yield  item

        nextPageText = response.xpath('//div[@id="pages"]/a/text()').getall()
        nextPageUrl = response.xpath('//div[@id="pages"]/a/@href').getall()
        for nextP in nextPageText:
            xiyiye = '下一页»'
            if nextP == xiyiye:
                yield response.follow(nextPageUrl[-1],callback=self.parse)

        nextPages = response.xpath('//div[@class="boxs"]/ul/li/a/@href').getall()
        # print(nextPages)
        for next in nextPages:
            x = True
            for p in ['3186.html','4622.html','5514.html','5839.html','9258.html','9252.html','9252.html','9243.html','9250.html']:
                if next.split('/')[-1] == p:
                    x = False
                    break
                else:
                    x = True

            if(x == True):
                print(next)
                yield response.follow(next, callback=self.parse)
