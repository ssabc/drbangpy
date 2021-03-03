import scrapy
class mingyanSpider(scrapy.Spider):
    name = "menus" 
    start_urls = [
        'https://www.huabaike.com/',
    ]

    def parse(self, response):
        for menu in response.css('div.rightmenubox a'):
            yield {
                'name': menu.css('::text').extract_first(),
                'href': menu.css('::attr("href")').extract_first()
            }

    def parse(self, response):
        for menu in response.css('ul.wzRcontent li'):
            yield {
                'name': menu.css('a::text').extract_first(),
                'href': menu.css('a::attr("href")').extract_first(),
                'redu': menu.css('span.redu_yhzs::text').extract_first(),
            }