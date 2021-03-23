import scrapy
from ..items import InternAssignItem

class WebspiderSpider(scrapy.Spider):
    n=0
    name = 'webspider'
    allowed_domains = ['houseofindya.com']
    start_urls = [
        'https://www.houseofindya.com/zyra/necklace-sets/short-necklace-sets/cat'
    ]

    def parse(self, response):
        items= InternAssignItem()
        lst=["short-necklace-sets","medium-necklace-sets","long-necklace-sets","choker-necklace-sets","pendant-sets"]
        product_name = response.css("#JsonProductList p").css("::text").extract()
        product_price=response.css("#JsonProductList span:nth-child(1)").css("::text").extract()
        product_image_url=response.css("#JsonProductList .lazy").css("::attr(src)").extract()


        items["product_category"]=lst[WebspiderSpider.n]
        items["product_name"] = product_name
        items["product_price"] = product_price
        items["product_image_url"] = product_image_url

        yield items
        WebspiderSpider.n+=1
        next_page="https://www.houseofindya.com/zyra/necklace-sets/"+lst[WebspiderSpider.n]+"/cat"
        yield response.follow(next_page, callback= self.parse)




