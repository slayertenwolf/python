# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DownloadpicsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #pass   #this line ###
    image_urls = scrapy.Field()               #add this line
   # images = scrapy.Field()                   #add this two lines
