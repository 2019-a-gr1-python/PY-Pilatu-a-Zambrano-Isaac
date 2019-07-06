import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from python_03.items import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class AraniaProductosFybeca(CrawlSpider):
    name = 'crawl_fybeca'
    allowed_domains = [
        'fybeca.com'
    ]
    start_urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=0&pp=25'
    ]
    url_segmento_permitido = (
        '.+(cat=238&s=[0-9]+&pp=25)$'
    )
    
    rules = (
        Rule(
            LinkExtractor(
            ), callback = 'parse'
        ),
    )
    
    

    def parse(self, response):

        productos = response.css('div.product-tile-inner')

        for producto in productos:
            existe_producto = producto.css('div.detail')

            if(len(existe_producto) > 0):
                producto_loader=ItemLoader(
                    item=ProductoFybeca(),
                    selector=producto
                )
                producto_loader.add_css(
                    'titulo',
                    'a.name::text'
                )
                producto_loader.add_xpath(
                    'imagen',
                    'div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src'
                )

                yield producto_loader.load_item()