from scrapy.spiders  import Spider
from scrapy.selector import Selector
from cl_test1.items  import CraigsListItem

import scrapy
import sys

class Craigslist(Spider):
    name = "craigslist"
    allowed_domains = []
    start_urls      = []

    def usage(self):
        print "Usage: scrapy crawl craigslist --nolog -a url=\"<some url>\" -a category=<category|list>"
        pass

    def __init__(self, url=None, category=None, *args, **kwargs):
        super(Craigslist, self).__init__(*args, **kwargs)
        try:
            if url == None:
                print "please provide a url"
                raise Exception()
            if (url.find("http://") == -1 and url.find("https://") == -1):
                print "please provide a full url with http:// or https://"
                raise Exception()

            if category == 'list':
                print "list feature not supported yet."
            elif category != None and len(category) != 3:
                print "category must be 3 letters"
                raise Exception()
            elif category != None:
                url = url + "/search/" + category

            print "crawling: " + url
            self.url             = url
            self.category        = category
            parts                = url.replace("http://", "").replace("https://", "").split('/')
            domain               = parts[0]
            self.allowed_domains = ['%s' % domain]
            self.start_urls      = ['%s' % url]
        except:
            self.usage()
            sys.exit()    # is there a better way?
        print "..."
        pass

    def parse(self,response):
        print response.url
        sel = Selector(response)
        items = []
        if self.category == 'list':
            print "list feature not supported yet."
        else:
            container_lists = sel.xpath('//li[@class="result-row"]')
            for li in container_lists:
                item = CraigsListItem()
                #item['ad_title']       = li.xpath('div[@class="title"]/a/text()').extract()
                #item['ad_location']    = li.xpath('div[@class="category-location"]/span/text()').extract()
                #item['ad_time']        = li.xpath('div[@class="info"]/div[@class="creation-date"]/span/text()').extract()
                item['ad_description'] = li.xpath('p/a/text()').extract()
                items.append(item)
        return items