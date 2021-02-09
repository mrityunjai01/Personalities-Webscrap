import scrapy
import os

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://google.com/search?q=sachin',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


class GoogleSpider():
    def __init__(self, name="sachin", testcase = 1, outfile="description", **kwargs):
        self.start_urls = [
            'https://google.com/search?q='+'+'.join(name.split()),
        ]
        self.name = f"case{str(testcase)}"
        self.outfile_d = os.path.join("data", "po"+outfile)
        self.outfile_l = os.path.join("data", "link_"+outfile)
    def getSpider(self):
        outfile_d = self.outfile_d
        outfile_l = self.outfile_l
        class RealSpider(scrapy.Spider):
            custom_settings = {'ROBOTSTXT_OBEY': False}
            def getHTMLText(self, response):
                print("I got a response", response)
                with open(outfile_d, 'a') as f:
                    f.writelines(response.url + "\n")
            def parse(self, response):
                listoflinks = response.xpath('//*[@id="main"]/div/div/div/a[starts-with(@href,\'/url\')]/@href').getall()
                description = response.xpath('//*[@id="main"]/div/div/div/div[1]/div[2]/div/div/div/div/text()').get()
                if description is None:
                    description=""
                with open(outfile_l, 'a') as f:
                    f.writelines(description+"\n")
                print("The list of links is ", listoflinks)
                yield from response.follow_all(urls = listoflinks, callback=self.getHTMLText)
        RealSpider.name = self.name
        RealSpider.start_urls = self.start_urls
        return RealSpider
