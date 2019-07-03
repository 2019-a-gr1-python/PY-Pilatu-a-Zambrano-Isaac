fetch('https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=0&pp=25')
contenedor=response.css('div.product-tile-inner')
url = response.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
titulo = contenedor.css('a.name::text')

class ProductoFybeca(scrapy.Item):
    titulo=scrapy.Field()
    imagen=scrapy.Field()
primer_producto=ProductoFybeca()
primer_producto['titulo']=titulo.extract_first()
primer_producto['imagen']=url.extract_first()
primer_producto

def transformar_url_imagen(texto):
    url='https://www.fybeca.com'
    cadena_a_reemplazar='../..'
    return texto.replace(cadena_a_reemplazar,url)

from scrapy.loader.processors import MapCompose, Join
class ProductoFybeca(scrapy.Item):
    titulo=scrapy.Field()
    imagen=scrapy.Field(
       input_processor=MapCompose(transformar_url_imagen),
       output_processor=Join(),
    )

il = ItemLoader(item=ProductoFybeca())
il.add_value('imagen',url.extract_first())
il.add_value('titulo',titulo.extract_first())
il.load_item()

%history -f archivo.py
