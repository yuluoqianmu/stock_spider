# -*- coding: utf-8 -*-
import scrapy

class TonghuashunSpider(scrapy.Spider):
    name = 'tonghuashun'
    allowed_domains = ['stockpage.10jqka.com.cn']
    start_urls = ['http://stockpage.10jqka.com.cn/HK2858/manager/']

    def parse(self, response):
        ## //*[@id="introduce"]/div[2]/table[1]
        names = response.xpath("//*[@class=\"m_table ggintro pr\"]/thead/tr/td/h3/text()").extract()
        for name in names:
            print(name)
        pass
