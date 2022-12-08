from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re

from search_jobs.items import Job
from search_jobs.util import extract_key


class CrowdWorksSpider(CrawlSpider):
    name = "cw"
    allowed_domains = ["crowdworks.jp"]

    def __init__(self, search_word=None, *args, **kwargs):
        super(CrowdWorksSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            f"https://crowdworks.jp/public/jobs/search?search%5Bkeywords%5D={search_word}&keep_search_criteria=true&order=score&hide_expired=true",
        ]

        self.rules = [
            Rule(LinkExtractor(allow=r"/public/jobs/\d{7}$"), callback="parse_job"),
        ]
        # 以下の処理がないと、rulesが反映されない
        self._compile_rules()

        print("\n\n\n")
        print(self.start_urls)

    def parse_job(self, response):
        title = response.css(".title_container > h1::text").get().strip()
        reward_type = response.css(".thead_nowrap tr:nth-child(1) div::text").get()
        price = response.css(".fixed_price_budget::text").get()
        publication_date = response.css(".thead_nowrap tr:nth-child(3) td::text").get()
        deadline = response.css(".thead_nowrap tr:nth-child(4) td::text").get()
        recruitment = response.css(".application_status_table tr:nth-child(3) td::text").get().strip()
        detail_info = " ".join(response.css(".confirm_outside_link::text").getall()).strip()
        unique_key = extract_key(response.url)

        print(f"仕事名：{title}")

        item = Job(
            url=response.url,
            key=unique_key,
            job_title=title,
            publication_date=publication_date,
            application_deadline=deadline,
            recruitment_number=recruitment,
            reward_type=reward_type,
            price=price,
            job_detail=detail_info,
        )

        yield item
