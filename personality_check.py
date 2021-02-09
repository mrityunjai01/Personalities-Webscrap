import argparse
from spiders.quotes_spider import GoogleSpider
from scrapy.crawler import CrawlerProcess

def check(input_text, outfile):

    process = CrawlerProcess()

    testcase = 0
    input_text = input_text.splitlines()
    for line in input_text:
        line = line.strip('\n')
        line = line.split(', ')
        print(f'Crawling for {line[0]}')
        process.crawl(GoogleSpider(line[0], testcase, outfile).getSpider())
        testcase+= 1

    process.start()
