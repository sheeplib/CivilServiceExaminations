# -*- coding: utf-8 -*-
"""
crawler for FuJian civil servent pisition
Created on Thu Mar 22 11:29:57 2018

@author: sheeplib
"""

import scrapy
from lxml import etree
from FuJianCivilServentPositionSpider.items import FujiancivilserventpositionspiderItem

class FuJianCivilServentPositionSpider(scrapy.Spider):
    
    name = "FuJianCivilServentPositionSpider"
    allowed_domains = ["fjkl.gov.cn"]
    start_urls = ["http://www.fjkl.gov.cn/"]
    
    page_range = range(1, 311)
    
    def start_requests(self):
        first_page_url = 'http://www.fjkl.gov.cn/z/api.aspx?action=PositionSearch&page=1&unitCode=&unitName=&unitType=&unitArea=&unitLevel=&positionCode=&positionName=&departmentId=&examType=&eduStatus=&hJLocation=&sex=&jobYear=&nation=&degree=&eduType=&specialPosition=&specialXQPosition=&specialty=&number=&age=&jsoncallback=jQuery191022529621592299742_1521431180255&_=1521431180256'
# 分离page之前的url串
        try:
            page_pos = first_page_url.find('page=')
            page_pos += 5
            url_before_page = first_page_url[:page_pos]
            url_after_page = first_page_url[page_pos:-1]
            # print(url_before_page)
        except:
            print('找不到关键字‘page=’')
# 分离page之后的url串    
        try:
            after_page_pos = url_after_page.find('&')
            url_after_page = url_after_page[after_page_pos:-1]
            # print(url_after_page)
        except:
            print('找不到关键字‘&’')
# parse first page
        # yield scrapy.Request(first_page_url, callback = self.parse)
        for page in self.page_range:
            yield scrapy.Request(url = url_before_page + str(page) + url_after_page, callback = self.parse)

    def parse(self, response):
        item = FujiancivilserventpositionspiderItem()
        positions = response.xpath('//div')
        # print(danweis)
        for position in positions:
            # tmp = danwei.xpath(r'table/tr[1]/td[2]/text()').extract_first()
            # print(tmp)
            # yield {'danwei':tmp, 'biaoji':'aaa'}
            item['workplace'] = position.xpath(r'table/tr[1]/td[2]/text()').extract_first()
            item['position'] = position.xpath(r'table/tr[1]/td[4]/text()').extract_first()
            item['system'] = position.xpath(r'table/tr[2]/td[2]/text()').extract_first()
            item['region'] = position.xpath(r'table/tr[2]/td[4]/text()').extract_first().split(' ')[0]
            item['level'] = position.xpath(r'table/tr[2]/td[4]/text()').extract_first().split(' ')[-1].split('：')[-1]
            item['site'] = position.xpath(r'table/tr[3]/td[2]/text()').extract_first()
            item['gradebenifit'] = position.xpath(r'table/tr[3]/td[4]/text()').extract_first()
            item['examtype'] = position.xpath(r'table/tr[4]/td[2]/text()').extract_first()
            item['recruit'] = position.xpath(r'table/tr[4]/td[4]/text()').extract_first()
            item['allowedregion'] = position.xpath(r'table/tr[5]/td[2]/text()').extract_first()
            item['age'] = position.xpath(r'table/tr[5]/td[4]/text()').extract_first()
            item['sex'] = position.xpath(r'table/tr[6]/td[2]/text()').extract_first()
            item['race'] = position.xpath(r'table/tr[6]/td[4]/text()').extract_first()
            item['party'] = position.xpath(r'table/tr[7]/td[2]/text()').extract_first()
            item['education'] = position.xpath(r'table/tr[7]/td[4]/text()').extract_first()
            item['degree'] = position.xpath(r'table/tr[8]/td[2]/text()').extract_first()
            item['educationtype'] = position.xpath(r'table/tr[8]/td[4]/text()').extract_first()
            item['experience'] = position.xpath(r'table/tr[9]/td[2]/text()').extract_first()
            item['specialposition'] = position.xpath(r'table/tr[9]/td[4]/text()').extract_first()
            item['major'] = position.xpath(r'table/tr[10]/td[2]/text()').extract_first()
            item['introduction'] = position.xpath(r'table/tr[11]/td[2]/text()').extract_first()
            item['others'] = position.xpath(r'table/tr[12]/td[2]/text()').extract_first()
            item['contact'] = position.xpath(r'table/tr[13]/td[2]/text()').extract_first()
            yield item
        
