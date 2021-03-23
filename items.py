# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InternAssignItem(scrapy.Item):
    # define the fields for your item here like:
    product_category=scrapy.Field()
    product_name = scrapy.Field()
    product_price = scrapy.Field()
    product_image_url = scrapy.Field()
    pass
