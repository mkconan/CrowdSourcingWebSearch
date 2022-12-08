# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Job(scrapy.Item):
    url = scrapy.Field()
    key = scrapy.Field()
    job_title = scrapy.Field()
    publication_date = scrapy.Field()  # 掲載日
    application_deadline = scrapy.Field()  # 応募期限日
    recruitment_number = scrapy.Field()  # 募集人数
    reward_type = scrapy.Field()  # 報酬タイプ
    price = scrapy.Field()  # 報酬額
    job_detail = scrapy.Field()  # 仕事の詳細
