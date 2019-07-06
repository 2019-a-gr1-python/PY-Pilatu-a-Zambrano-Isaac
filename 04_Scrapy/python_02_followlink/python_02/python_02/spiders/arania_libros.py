import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlBook(CrawlSpider): 
    name = 'crawl_book'
    allowed_domains = [
        'toscrape.com'
    ]
    start_urls = [
        'http://books.toscrape.com/index.html'
    ]
    url_segmento_permitido = (
        'category/books/fantasy_19',
        'category/books/mystery_3',
        'category/books/religion_12'
    )
    rules = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = url_segmento_permitido
            ), callback = 'parse_page'
        ),
    )
    def parse_page(self, response):
        lista_nombres = response.css('article.product_pod > h3 > a::attr(title)').extract()

        for nombre in lista_nombres:
            with open('book_nombre.txt', 'a+') as archivo:
                archivo.write(nombre + '\n')