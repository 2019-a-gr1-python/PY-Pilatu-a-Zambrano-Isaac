# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst
import re
def limpiar_precio(precio_str):
    precio_string=re.search(r'[+-]?\d+(?:\.\d+)?',precio_str).group(0)
    return float(precio_string)


def limpiar_nombre(nombre_str):
    return nombre_str.replace('\n','').strip() 


class ProyectoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ProductoMueble(scrapy.Item):
    nombre=scrapy.Field(
        input_processor=MapCompose(limpiar_nombre),
        output_processor=TakeFirst()
        )
    precio_regular = scrapy.Field(
        input_processor=MapCompose(limpiar_precio),
        output_processor=TakeFirst()
        )
    precio_oferta = scrapy.Field(
        input_processor=MapCompose(limpiar_precio),
        output_processor=TakeFirst()
        )
    categoria = scrapy.Field(output_processor=TakeFirst())
    empresa = scrapy.Field(output_processor=TakeFirst())