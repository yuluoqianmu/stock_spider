# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
class StockSpiderPipeline(object):
    def process_item(self, item, spider):
        return item

class StockPipeline(object):
    # 类被加载时要创建一个文件
    def __init__(self):
        self.file = open("executive_pre.csv", "a+")

    def process_item(self, item, spider):

        # 判断文件是否为空，为空写titile
        if os.path.getsize("executive_pre.csv"):
            #开始写文件
            self.write_content(item)
        else:
            self.file.write("高管姓名,性别,年龄,股票代码,职位\n")
        self.file.flush()
        return item

    def write_content(self, item):
        names = item["names"]
        sexs = item["sexs"]
        ages = item["ages"]
        code = item["code"]
        leaders = item["leaders"]
        result = ""
        for i in range(len(names)):
            result = names[i]+","+ sexs[i]+","+ ages[i]+","+ code[i]+","+ leaders[i]+"\n"
            self.file.write(result)