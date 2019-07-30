import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from proyecto.items import ProductoMueble
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class AraniaProductosBosque(CrawlSpider):
    name = 'crawl_bosque'
    allowed_domains = [
        'bosque.com'
    ]
    start_urls = [
        'https://www.bosque.com.ec/dormitorios',
        'https://www.bosque.com.ec/salas',
        'https://www.bosque.com.ec/comedores'
    ]
    url_segmento_permitido = (
        '#[0-9]+'
    )
    
    rules = (
        Rule(
            LinkExtractor(
                allow= (url_segmento_permitido,)
            ), callback = 'parse'
        ),
    )
    
    

    def parse(self, response):
        categoria=response.css('div.showcase-default>h2.titulo-sessao::text').extract_first()
        productos = response.css('li>div.box-item')

        for producto in productos:
            existe_producto = producto.css('div.data')

            if(len(existe_producto) > 0):
                producto_loader=ItemLoader(
                    item=ProductoMueble(),
                    selector=producto
                )
                producto_loader.add_css(
                    'nombre',
                    'div.data>h3.product-name>a::attr(title)'
                )
                producto_loader.add_css(
                    'precio_regular',
                    'div.data>p.price>a>span.oldPrice>span.finalOldPrice::text'
                )
                producto_loader.add_css(
                    'precio_oferta',
                    'div.data>p.price>a>span.bestPrice::text'
                )
                producto_loader.add_value(
                    'categoria',
                    categoria
                )
                producto_loader.add_value(
                    'empresa',
                    'El Bosque'
                )

                yield producto_loader.load_item()