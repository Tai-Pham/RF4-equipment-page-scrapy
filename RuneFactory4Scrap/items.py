# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Runefactory4ScrapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	
	type = scrapy.Field();
	name = scrapy.Field();
	abilities = scrapy.Field();
	buy = scrapy.Field();
	sell = scrapy.Field();
	description = scrapy.Field();
	
	
	#pass
