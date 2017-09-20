import scrapy

class DmozSpider(scrapy.Spider):
    name = "Dmoz"
    allowed_domains = ["yatang.cn"]
    start_urls = ["https://www.yatang.cn/"]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename,'wb').write(response.body)