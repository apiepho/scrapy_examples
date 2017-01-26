from scrapy.spiders  import Spider
from scrapy.selector import Selector
from cl_test1.items  import CraigsListItem

import scrapy
import sys

class Craigslist(Spider):
    name = "craigslist"
    allowed_domains = []
    start_urls      = []
    totalcount      = 0
    currentcount    = 0

    def usage(self):
        print "Usage: scrapy crawl craigslist -a url=\"<some url>\" -a category=<category|list> --nolog"
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

        # check for list, if so, list all categories from main page
        if self.category == 'list':
            print "listing categories:"
            container_lists = sel.css('a')
            for li in container_lists:
                if li.extract().find("data-cat") != -1:
                	sym  = li.css('a::attr(class)').extract()[0]
                	href = li.css('a::attr(href)').extract()[0]
                	desc = li.css('span::text').extract()[0]
                	print("%-30s%-10s%s" % (desc, sym, href))
            return

        # check for first page of a category, if so, find total and start sequence of pages
        elif response.url.find('?s=') == -1:
            self.totalcount = int(sel.css('span[class=totalcount]::text').extract()[0])
            print("totalcount  : %d" % self.totalcount)
            next_page = "?s=%d" % self.currentcount
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            return
            
        # this should be one of the sequence of pages, parse items and start next page
        else:
            # select all rows
            container_lists = sel.css('li[class="result-row"]')
            for li in container_lists:
                # build item
                item = CraigsListItem()
                item['description'] = li.css('p a::text').extract()[0]
                item['location']    = li.css('p a::attr(href)').extract()[0]
                item['time']        = li.css('p time::attr(datetime)').extract()[0]
                items.append(item)

            # yield items, cannot use 'return items' because we are using yield and generators for next page
            for item in items:
                yield item
                
            # update count and start next page
            self.currentcount += 100
            if self.currentcount < self.totalcount:
                next_page = "?s=%d" % self.currentcount
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
                return

        # done
        return



