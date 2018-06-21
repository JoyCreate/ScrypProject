import  scrapy
from scrapy import  Selector
from  scrapy import  Request
import  sys
sys.path.append("D:\\python27File")
sys.path.append("D:\\python27File\\NewScrapySpider")
sys.path.append("D:\\python27File\\NewScrapySpider\\NewScrapySpider")
sys.path.append("D:\\python27File\\NewScrapySpider\\NewScrapySpider\\spiders")
class NgaSpider(scrapy.Spider):
    name = 'NgaSpider'
    host='http://crm2.icvip.com/'
    start_urls=['http://crm2.icvip.com/',]
    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url,callback=self.parse_page)
    def parse_page(self, response):
        selector=Selector(response)
        content_list=selector.xpath('//*[@id="guidePage"]/section[1]/ul/li[2]/p/a[1]')
        print(content_list)
        for content in  content_list:
            topic=content.xpath('//*[@id="guidePage"]/section[1]/ul/li[2]/p/a[1]').extract_first()
            print(topic)
            url=self.host+content.xpath('//*[@id="guidePage"]/section[1]/ul/li[2]/p/a[1]').extract_first()
            yield Request(url=url,callback=self.parse_topic)
    def parse_topic(self, response):
        selector=Selector(response)
        content_list=selector.xpath('//*[@id="guidePage"]/section[1]/ul/li[2]/p/a[1]')
        for contens in content_list:
            contens=contens.xpath('//*[@id="guidePage"]/section[1]/ul/li[2]/p/a[1]').extract_first()
            item=Content()
            item['url']=response.url
            item['content']=contens
            item['']=''
            yield item
            print(contens)
