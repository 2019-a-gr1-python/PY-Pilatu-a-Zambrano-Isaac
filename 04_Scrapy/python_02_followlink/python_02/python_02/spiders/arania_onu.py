import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 

class AraniaONU(CrawlSpider):
    name='crawl_onu_spider' #Heredado conservar nombre de atributo
    allowed_domains = [     #Heredado conservar nombre de atributo
        'un.org'
        ]
    start_urls=[    #Heredado conservar nombre de atributo
        'http://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html'
        ]
    url_segmentos_permitidos=('funds-programmes-specialized-agencies-and-others')
    url_segmentos_restringidos=(
        'ar/sections',
        'zh/sections',
        'ru/sections'
    )
    rules=(
        Rule(LinkExtractor(
            allow_domains=allowed_domains,
            allow=url_segmentos_permitidos,
            deny=url_segmentos_restringidos,
        ),callback='parse_page'),
    )

    def parse_page(self, response):
        lista_programas=response.css('div.field-items > div.field-item.even > h4::text').extract()
        for programa in lista_programas:
            with open('onu_agencias.txt','a+') as archivo:
                archivo.write(programa+'\n')