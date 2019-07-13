# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import pandas as pd

class FiltrarSoloCapsulas(object):

    def process_item(self, item, spider):
        titulo=item['titulo']
        if ('capsula' not in titulo):
            raise DropItem('No tiene capsula en el título')
        else:
            return item


class TransformarTituloAMinusculas(object):
    
    def process_item(self, item, spider):
        titulo=item['titulo']
        titulo=titulo.lower()
        item['titulo']=titulo
        return item

class FiltrarSuperiores(object):
    productos= pd.read_csv('tmp/productos-fybeca.csv',delimiter=',')
    promedio=productos['precio'].mean()
    def process_item(self, item, spider):
        precio=item['precio']
        if (precio < promedio):
            raise DropItem('Descartado producto con precio menor al promedio')
        else:
            return item