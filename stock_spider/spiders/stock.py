# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import re
from stock_spider.items import StockItem

class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['pycs.greedyai.com']
    start_urls = ['http://pycs.greedyai.com/']

    def parse(self, response):
        post_urls = response.xpath("//a/@href").extract()
        for post_url in post_urls:
          yield scrapy.Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail, dont_filter=True)
        pass

    #回调函数处理页面详细信息
    def parse_detail(self, response):
        stock_item = StockItem()
        #抓取姓名信息
        stock_item["names"] = self.get_names(response)
        #抓取性别信息
        stock_item["sexs"] = self.get_sex(response)
        #抓取年龄信息
        stock_item["ages"] = self.get_age(response)
        #股票代码
        stock_item["code"] = self.get_code(response)
        #职位信息
        stock_item["leaders"] = self.get_leader(response, len(stock_item["names"]))
        #文件存储逻辑
        yield stock_item


    def get_names(self, response):
        names = response.xpath("//*[@id=\"ml_001\"]/table/tbody/tr[1]/td[1]/a/text()").extract()
        return names

    def get_sex(self, response):
        infos = response.xpath("//*[@class=\"intro\"]/text()").extract()
        sex_list = []
        for info in infos:
            try:
                sex = re.findall("[男|女]", info)[0]
                sex_list.append(sex)
            except(IndexError):
                continue
        return sex_list

    def get_age(self, response):
        infos = response.xpath("//*[@class=\"intro\"]/text()").extract()
        age_list = []
        for info in infos:
            try:
                age = re.findall("\d+", info)[0]
                age_list.append(age)
            except(IndexError):
                continue
        return age_list

    def get_code(self, response):
        infos = response.xpath("/html/body/div[3]/div[1]/div[2]/div[1]/h1/a/@title").extract()
        code_list = []
        for info in infos:
            code = re.findall("\d+", info)[0]
            code_list.append(code)
        return code_list

    def get_leader(self, response, length):
        leaders = response.xpath("//*[@class=\"tl\"]/text()").extract()
        leaders = leaders[0:length]
        return leaders
