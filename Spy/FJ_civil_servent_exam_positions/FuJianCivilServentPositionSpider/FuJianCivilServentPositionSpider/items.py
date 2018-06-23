# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FujiancivilserventpositionspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    workplace = scrapy.Field()          # 单位代码/名称
    position = scrapy.Field()           # 职位代码/名称
    system = scrapy.Field()             # 单位所属系统
    region = scrapy.Field()             # 单位所属地区
    level = scrapy.Field()              # 单位层级
    site = scrapy.Field()               # 职位所在县区
    gradebenifit = scrapy.Field()       # 是否分数倾斜
    examtype = scrapy.Field()           # 试卷类型
    recruit = scrapy.Field()            # 招收人数
    allowedregion = scrapy.Field()      # 招考范围
    age = scrapy.Field()                # 年龄要求
    sex = scrapy.Field()                # 性别要求
    race = scrapy.Field()               # 民族要求
    party = scrapy.Field()              # 政治面貌要求
    education = scrapy.Field()          # 文化程度要求
    degree = scrapy.Field()             # 学位要求
    educationtype = scrapy.Field()      # 学历类别要求
    experience = scrapy.Field()         # 工作经验要求
    specialposition = scrapy.Field()    # 是否专门职位
    major = scrapy.Field()              # 所需专业
    introduction = scrapy.Field()       # 职位简介
    others = scrapy.Field()             # 其他
    contact = scrapy.Field()            # 联系方式
    
    
