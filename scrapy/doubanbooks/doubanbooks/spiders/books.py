# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["http://book.douban.com/"]
    start_urls = (
        'http://www.http://book.douban.com//',
    )

    def parse(self, response):
        pass
