class GeneradorURl():
    def generador_url_fybeca(self,categoria, maximo, step):
            urls_generadas=[]
            url_base='https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?'
            for i in range(0, maximo+1, step):
                url_nueva=url_base+'cat='+str(categoria)
                url_nueva+='&s='+str(i)
                url_nueva+='&pp='+str(step)+'&b=-1&ot=0'
                urls_generadas.append(url_nueva)
            return urls_generadas