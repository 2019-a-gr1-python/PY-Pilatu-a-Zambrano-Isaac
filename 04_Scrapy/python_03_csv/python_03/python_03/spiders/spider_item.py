import scrapy
from python_03.items import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class AraniaProductosFybeca(scrapy.Spider):
    name = 'arania_fybeca'


    def start_requests(self):
        urls=[
            'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=0&pp=25'
        ]

        for url in urls:
            yield scrapy.Request(url=url)


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