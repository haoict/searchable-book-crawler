# -*- coding: utf-8 -*-
# encoding=utf8
import sys
import scrapy
from collections import namedtuple
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join

reload(sys)
sys.setdefaultencoding('utf8')

class TimsachSpider(scrapy.Spider):
    name = 'timsach'
    allowed_domains = ['timsach.top']
    # start_urls = ['http://timsach.top/']

    def start_requests(self):
        base_url = 'http://timsach.top/ebook/'
        # urls = [
        #     'http://timsach.top/ebook/8.html',
        #     'http://timsach.top/ebook/10.html',
        # ]
        for i in range(1, 50):
            yield scrapy.Request(url=base_url + str(i) + '.html', callback=self.parse)

    def parse(self, response):
        try:
            page = response.url.split("/")[-1].split(".")[0]
            self.log('ID: %s' % page)

            book_name = response.css('h2::text').extract_first()
            #self.log('book_name: %s' % book_name)

            book_author = response.css('h4::text').extract_first().replace('Tác giả: ', '')
            #self.log('book_author: %s' % book_author)

            book_category = response.css('h4 a::text').extract_first().replace('Thể loại: ', '')
            #self.log('book_category: %s' % book_category)

            book_cover = response.xpath('//img[@class="img-thumbnail"]//@src').extract_first()
            # BookDownload = namedtuple('BookDownload', ['source', 'epub', 'mobi', 'pdf', 'azw3', 'prc'])
            # book_downloads = []
            # for book_download in response.css('div.book-download'):
            #     # print(book_download.css('a::text').extract_first())
            #     # bd = BookDownload._fields_defaults
            #     source = book_download.css('a::text').extract_first()
            #     epub = book_download.css('a')[1].extract()
            #     # book_downloads.append(bd)
            #     self.log('source: %s' % source)
            #     self.log('epub: %s' % epub)
            # self.log('book_downloads: %s' % book_downloads)

            loader = ItemLoader(response=response)
            book_description = loader.get_xpath('//div[@class="book-description"]/node()', Join())
            #self.log('book_description: %s' % book_description)
        except:
            self.log('ERROR in: %s', response.url)

        yield {
            'id': page,
            'name': book_name,
            'author': book_author,
            'category': book_category,
            'description': book_description,
            'cover': book_cover
        }
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
