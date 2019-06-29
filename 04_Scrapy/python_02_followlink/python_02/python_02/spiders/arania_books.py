import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 

class AraniaBooks(CrawlSpider):
    name='crawl_books_spider' #Heredado conservar nombre de atributo
    allowed_domains = [     #Heredado conservar nombre de atributo
        'toscrape.com'
        ]
    start_urls=[    #Heredado conservar nombre de atributo
        'http://books.toscrape.com/index.html'
        ]
    url_segmentos_permitidos=(
        'category/books/fantasy_19',
        'category/books/mystery_3',
        'category/books/religion_12'
        )
    rules=(
        Rule(LinkExtractor(
            allow_domains=allowed_domains,
            allow=url_segmentos_permitidos
        ),callback='parse_page'),
    )

    def parse_page(self, response):
        lista_titulos=response.css('article.product_pod > h3 > a::attr(title)').extract()
        for titulo in lista_titulos:
            with open('titulos_books.txt','a+') as archivo:
                archivo.write(titulo+'\n')

                    