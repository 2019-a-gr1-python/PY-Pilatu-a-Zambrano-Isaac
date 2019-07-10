import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst
import re

def transformar_url_imagen(texto): 
    url = 'https://www.fybeca.com' 
    cadena_a_reemplazar = '../..'   
    return texto.replace(cadena_a_reemplazar,url)

def limpiar_precio(precio_str):
    precio_string=re.search(r'\((.*?)\)\.formatMoney',precio_str).group(1)
    return float(precio_string)

class ProductoFybeca(scrapy.Item):
    imagen = scrapy.Field(
        input_processor = MapCompose(
            transformar_url_imagen
            ),
            output_processor=TakeFirst()
    )
    titulo = scrapy.Field(
        output_processor=TakeFirst()
    )
    precio = scrapy.Field(
        input_processor = MapCompose(
            limpiar_precio
            ),
        output_processor=TakeFirst()
    )

    