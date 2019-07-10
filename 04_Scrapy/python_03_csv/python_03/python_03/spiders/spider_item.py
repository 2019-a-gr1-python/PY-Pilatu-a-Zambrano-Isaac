import scrapy
from python_03.items import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from python_03.spiders.funcion_url import GeneradorURl
class AraniaProductosFybeca(scrapy.Spider):
    name = 'arania_fybeca'


    

    def start_requests(self):
        urls= GeneradorURl.generador_url_fybeca(None,238,150,25)

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
                producto_loader.add_xpath(
                    'precio',
                    'div[contains(@class,"detail")]/ div[contains(@class,"side")]/ div[contains(@class,"price")]/@data-bind'
                )

                yield producto_loader.load_item()