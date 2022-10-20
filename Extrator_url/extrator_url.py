'''
Project: Extração de URL
Company: Alura - String em Python: extraindo informações de uma URL
By: Pedro Tiago Bernabé Lomas
WhatsApp: +55 (12) 98858-5806
LinkedIn: https://www.linkedin.com/in/pedro-lomas/
E-mail: ptiago.lomas@gmail.com
Create: 2022-10-20
Language: Python
Version: 3.10.5
***** Modified
By:
Date:
By:
Date:
By:
Date:
'''

''' ***** VARIAVEIS ***** '''
# Numéricas

# Booleanas

# Strings

# List

''' ***** REGRAS DE NEGOCIO ***** '''
'''

'''

''' ***** BIBLIOTECAS ***** '''
import re #Regular expressions

'''
*********************************
--> CLASSES
*********************************
'''

class URL:
    #CONSTRUTOR
    def __init__(self,url):
        self._url = url
        self._base = ""
        self._parametros = ""
        self.sanitiza_url()
        self.valida_url()
        self.get_url_base()
        self.get_url_parametros()

    #PROPRIEDADES
    @property
    def url(self):
        return self._url

    @property
    def base(self):
        return self._base

    @property
    def parametros(self):
        return self._parametros

    #DATA MODEL - COMPORTAMENTOS ESPECIAIS
    def __str__(self):
        return str(f"{self._url}")

    def __eq__(self,other):
        return self._url == other._url

    def __len__(self):
        return len(self._url)

    #MÉTODOS
    def sanitiza_url(self):
        self._url = self._url.replace(" ","")
        return self._url

    def valida_url(self):
        #Verifica se url esta vazia
        if not self._url: raise ValueError("URL inválida")

        #Verifica se url segue padrão
        padrao = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao.match(self._url)
        if not match: raise ValueError("URL inválida")

    def get_url_base(self):
        reg_1 = self._url.find("?")
        self._base = self._url[:reg_1]
        return self._base

    def get_url_parametros(self):
        reg_1 = self._url.find("?")
        self._parametros = self._url[reg_1+1:]
        return self._parametros

    def get_valor_parametro(self, parametro):
        reg_1 = self._parametros.find(parametro) #Procura o parametro no meio da URL
        reg_2 = reg_1 + len(parametro) + 1 #Indice aonde se inicia o valor
        reg_3 = self._parametros.find("&",reg_2) #Indice aonde termina o valor
        if reg_3 == -1:
            valor = self._parametros[reg_2:]
        else:
            valor = self._parametros[reg_2:reg_3]

        return valor

url_1 = URL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
url_2 = URL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")

print(url_1 == url_2)