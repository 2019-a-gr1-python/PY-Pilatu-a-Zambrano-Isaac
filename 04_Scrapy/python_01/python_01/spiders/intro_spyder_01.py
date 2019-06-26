import scrapy
import numyp as np
import pandas as pd
class IntroSpider(scrapy.Spider):
    name='introduccion_spider'

    def start_requests(self):
        urls=[
            'http://books.toscrape.com/catalogue/category/books_1/page-1.html'
        ]

        for url in urls:
            yield scrapy.Request(url=url)

    def parse(self,response):
        etiqueta_contenedora = response.css('article.product_pod')
        titulos=etiqueta_contenedora.css('h3 > a::attr(title)').extract()
        precios=etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()
        stocks=etiqueta_contenedora.css('div.product_price > p.instock.availability::text').extract()
        indices_stocks=np.arange(1,len(stocks),2) 
        stocks=stocks[indices_stocks]
        stocks=list(map(lambda x:x.strip(),stocks))
        dic={'Titulos':titulos,'Precios':precios,'Stocks':stocks}
        df=pd.DataFrame(data=dic)
        print(df)

