from scrapy.spiders  import Spider
from scrapy.selector import Selector
from gumtree.items   import GumtreeItem

class gumz(Spider):
    name = "gumz"
    allowed_domains = ["gumtree.sg"]
    start_urls = [
    "https://www.gumtree.sg/s-home-furnishing/v1c44p1"
    ]

    def parse(self,response):
         sel = Selector(response)
         container_lists = sel.xpath('//div[@class="container"]')
         items = []
         for li in container_lists:
             item = GumtreeItem()
             item['ad_title']       = li.xpath('div[@class="title"]/a/text()').extract()
             item['ad_location']    = li.xpath('div[@class="category-location"]/span/text()').extract()
             item['ad_time']        = li.xpath('div[@class="info"]/div[@class="creation-date"]/span/text()').extract()
             item['ad_description'] = li.xpath('div[@class="description"]/span/text()').extract()
             items.append(item)
         return items