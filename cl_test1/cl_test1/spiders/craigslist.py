from scrapy.spiders  import Spider
from scrapy.selector import Selector
from cl_test1.items  import CraigsListItem

class cars(Spider):
    print "AAAA crawling: " + self.args
    name = "craigslist"
    allowed_domains = ["fortcollins.craigslist.org"]
    start_urls = [
    "https://fortcollins.craigslist.org/search/cto"
    ]

    def __init__ (self, domain=None, player_list=""):
        self.allowed_domains = ['sports.yahoo.com']
        self.start_urls = [
            'http://sports.yahoo.com/nba/players',
        ]
        self.player_list= "%s" % player_list

    def parse(self,response):
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