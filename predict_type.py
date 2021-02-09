import argparse
from spiders.quotes_spider import GoogleSpider
from scrapy.crawler import CrawlerProcess
parser = argparse.ArgumentParser()
parser.add_argument('--testcase', type=int, help="the number of testcases")
parser.add_argument('--inputfile', type=str, help="the input file")

args = parser.parse_args()

print(f"What i got as arguments, testcase = {args.testcase} and inputfile = {args.inputfile}")

process = CrawlerProcess()

with open(args.inputfile) as f:
    testcase = 0
    for line in f:
        line = line.strip('\n')
        line = line.split(', ')
        print(f'Crawling for {line[0]}')
        process.crawl(GoogleSpider(line[0], testcase).getSpider())
        testcase+= 1

process.start()
