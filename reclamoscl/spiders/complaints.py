# -*- coding: utf-8 -*-
import scrapy

class ComplaintSpider(scrapy.Spider):
    name = "reclamos"
    start_urls = [
        'http://www.reclamos.cl/',
    ]

    def parseComplaint(self,response):
        category = response.css('div#main div.breadcrumb a::text')
        if len(category) != 3:
            category = [u'NN']
        else:
            category = [category.extract()[1]]
        yield {
            'title' : ' - '.join(response.css('h1.reclamo-front-title span::text').extract()).encode('utf-8'),
            'complaint' : ' '.join(response.css('div.node-content p::text').extract()).encode('utf-8'),
            'date' : response.css('div.node-info span::text').extract_first().encode('utf-8'),
            'category' : category[0].encode('utf-8'),
            'url': response.url.encode('utf-8')
        }

    def parse(self, response):
        for complaint in response.css('div#reclamos-recientes tr'):
            detail = complaint.css('td a::attr(href)').extract_first()
            yield scrapy.Request(response.urljoin(detail), callback=self.parseComplaint)

        #next_page = response.css('div.pager a[title*=siguiente].pager-next.active::attr(href)').extract_first()
        
        next_page = response.css("span.pager-list+a.active::attr(href)").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)