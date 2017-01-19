import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    '''
    # alternative that sets default start_urls and relies on "parse" being the default Request callback
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
    '''

    '''
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    '''

    def parse(self, response):
        '''
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        '''

        '''
        # can use interactive mode to test expressions
        #  scrapy shell 'http://quotes.toscrape.com/page/1/'
        print("AAAA in parse for %s" % (response.url))
        print(  "   title text: %s" % ( response.css('title::text').extract_first() )  )
        print(  "   title text: %s" % ( response.xpath('//title') )  )
        print(  "   title text: %s" % ( response.xpath('//title/text()').extract_first() )  )
        for quote in response.css("div.quote"):
            text = quote.css("span.text::text").extract_first()
            author = quote.css("small.author::text").extract_first()
            tags = quote.css("div.tags a.tag::text").extract()
            print(dict(text=text, author=author, tags=tags))
        '''

        '''
        print(  "%s" % ( response.css('li.next a').extract_first() )  )
        print(  "%s" % ( response.css('li.next a::attr(href)').extract_first() )  )
        '''
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)


