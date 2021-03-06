from scrapy.spiders  import Spider
from scrapy.selector import Selector
from cl_test1.items  import CraigsListItem

class cars(Spider):
    name = "cars"
    allowed_domains = ["fortcollins.craigslist.org"]
    start_urls = [
    "https://fortcollins.craigslist.org/search/cto"
    ]

    def parse(self,response):
        print self.args
        sel = Selector(response)
        container_lists = sel.xpath('//li[@class="result-row"]')
        items = []
        for li in container_lists:
            item = CraigsListItem()
            #item['ad_title']       = li.xpath('div[@class="title"]/a/text()').extract()
            #item['ad_location']    = li.xpath('div[@class="category-location"]/span/text()').extract()
            #item['ad_time']        = li.xpath('div[@class="info"]/div[@class="creation-date"]/span/text()').extract()
            item['ad_description'] = li.xpath('p/a/text()').extract()
            items.append(item)
        return items