FROM python:3
USER root

RUN apt-get update
RUN apt-get -y upgrade

RUN mkdir /root/search_jobs
WORKDIR /root/search_jobs

RUN pip3 install requests scrapy pymongo python-dotenv

CMD [ "scrapy", "crawl", "cw", "-a", "search_word=スクレイピング" ]