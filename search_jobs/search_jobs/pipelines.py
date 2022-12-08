# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
from dotenv import load_dotenv
from itemadapter import ItemAdapter
from pymongo import MongoClient
import requests

from search_jobs.util import extract_key

load_dotenv()
SLACK_INCOMING_WEBHOOK_URL = os.environ["SLACK_INCOMING_WEBHOOK_URL"]


class MongoPipeline:
    def open_spider(self, spider):
        self.client = MongoClient("mongo", 27017, username="root", password="example")
        self.db = self.client["scraping-job"]
        self.collection = self.db["items"]
        self.collection.create_index("key", unique=True)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        key = extract_key(item["url"])

        job = self.collection.find_one({"key": key})
        # 新しい仕事が追加された場合はSlackで通知する
        if not job:
            print("New job!!")
            requests.post(
                url=SLACK_INCOMING_WEBHOOK_URL,
                json={
                    "text": f'Title:\t{item["job_title"]}\nPrice:\t{item["price"]}\nURL:\t{item["url"]}',
                    "unfurl_links": True,
                },
            )
            self.collection.insert_one(dict(item))
        return item
