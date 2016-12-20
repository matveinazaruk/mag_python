# coding: utf-8
from __future__ import unicode_literals

import scrapy
import re
import urllib


class PhilosophySpider(scrapy.Spider):
    name = 'blogspider'

    start_urls = ['https://ru.wikipedia.org/wiki/Кошка']
    #start_urls = ['https://ru.wikipedia.org/wiki/Python']
    #start_urls = ['https://en.wikipedia.org/wiki/Los_Angeles']
    custom_settings = {
        'DOWNLOAD_DELAY': 2 
    }

    stop_links = [
        'https://ru.wikipedia.org/wiki/%D0%A4%D0%B8%D0%BB%D0%BE%D1%81%D0%BE%D1%84%D0%B8%D1%8F',
        'https://en.wikipedia.org/wiki/Philosophy'
    ]

    def parse(self, response):
        if response.url not in self.stop_links:
            next_url = ""
            for paragraph in response.xpath('//div[@id="bodyContent"]/div/p'):
                for url in paragraph.xpath('a'):
                    pattern = r'\([^\)]*' + re.escape(url.extract()) + '[^\(]*\)'
                    if not re.search(pattern, paragraph.extract()):
                        next_url = url.xpath('@href').extract_first()
                        break
                if next_url:
                    break
            print 'Next url is: ', urllib.unquote(str(next_url))
            yield scrapy.Request(response.urljoin(next_url), self.parse)
        else:
            print 'Come to philosophy page!'

            

