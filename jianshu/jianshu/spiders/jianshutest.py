# -*- coding: utf-8 -*-
from scrapy import Request,Spider


class JianshutestSpider(Spider):
    name = 'jianshutest'
    allowed_domains = ['jianshu.com']
    start_urls = ['http://jianshu.com/']


    def start_requests(self):
        url = 'https://www.jianshu.com/p/39097525e615'
        headers = {  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'    Accept-Encoding':'gzip, deflate, br',
'    Accept-Language':'zh-CN,zh;q=0.9',
'    Cache-Control':'max-age=0',
'    Connection':'keep-alive',

'    Host':'www.jianshu.com',
'    If-None-Match':'W/"a2bf45c7e139d5c5890a6d1ad6946052"',
'    Upgrade-Insecure-Requests':'1',
'    User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
 }
        cookie = {
        '_ga=GA1.2.958245445.1504323082; remember_user_token=W1s0ODkzMTA2XSwiJDJhJDEwJFZDQnRIQ2dPY1RRUndVMTcxOVRFV2UiLCIxNTEzOTQ1NzAzLjAwMTk2MDMiXQ%3D%3D--93b329408286f14dfa8bee38bd072e59d7e49ef3; _gid=GA1.2.1418083379.1514385925; read_mode=day; default_font=font2; locale=zh-CN; _m7e_session=a9a10258f2b80a2ac34940f82f49478e; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1514208114,1514208376,1514385925,1514447900; _gat=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%224893106%22%2C%22%24device_id%22%3A%2216082d5998c6f3-01395e664f4de3-b7a103e-2073600-16082d5998d394%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%2216082d5998c6f3-01395e664f4de3-b7a103e-2073600-16082d5998d394%22%7D; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1514447907'}

        yield Request(url,callback=self.parse,headers=headers)

    def parse(self, response):
        print(response.text)
