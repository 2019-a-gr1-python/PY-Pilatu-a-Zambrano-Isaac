import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from proyecto.items import ProductoMueble
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

class AraniaProductosPycca(CrawlSpider):
    name = 'crawl_pycca'
    allowed_domains = [
        'bosque.com'
    ]
    start_urls = [
        'https://www.pycca.com/muebles/dormitorio',
        'https://www.pycca.com/muebles/comedores',
        'https://www.pycca.com/muebles/sala'
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
        categoria=response.css('div.pyccaCategory__vitrine>h2.titulo-sessao::text').extract_first()
        productos = response.css('li>div.productVitrine')

        for producto in productos:
            existe_producto = producto.css('div.itemD')

            if(len(existe_producto) > 0):
                producto_loader=ItemLoader(
                    item=ProductoMueble(),
                    selector=producto
                )
                producto_loader.add_css(
                    'nombre',
                    'div.productVitrine>h4.pyccaCategory__vitrine__box__name>a::text'
                )
                producto_loader.add_css(
                    'precio_regular',
                    'div.productVitrine>div.pyccaCategory__vitrine__box__price.prices>p::text'
                )
                producto_loader.add_css(
                    'precio_oferta',
                    'div.productVitrine>div.pyccaCategory__vitrine__box__price.prices>p::text'
                )
                producto_loader.add_value(
                    'categoria',
                    categoria
                )
                producto_loader.add_value(
                    'empresa',
                    'Pycca'
                )

                yield producto_loader.load_item()