'''
Project: Jogo da Forca
Company: Alura - Python: avançando na linguagem
By: Pedro Tiago Bernabé Lomas
WhatsApp: +55 (12) 98858-5806
LinkedIn: https://www.linkedin.com/in/pedro-lomas/
E-mail: ptiago.lomas@gmail.com
Create: 2022-10-13
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


'''
*********************************
--> CLASSES
*********************************
'''

class Conta():
    #***Métodos estáticos da classe
    NomeBanco = "Pedro'sBank"

    @staticmethod
    def codigoBanco():
        return 123

    #***Criação dos atributos da classe
    #A função __init__(self) cria um objeto/instância da classe com os atríbutos abaixo
    def __init__(self,numero,titular,saldo,limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #***Métodos da classe
    #Usar verbos no infinitivo para nomes de métodos
    #Usar camelCase para nomenclatura
    #Métodos que mexem exclusivamente com apenas um atributo, usar tudo minusculo no nome
    #Usar na nomenclatura do método como prefixo:
    # get  = OUTPUT = para pegar a informação do sistema para o usuário
    # set  = INPUT  = para o usuário passar para o sistema a informação
    # show = para o sistema apenas exibir a informação sem altera-lá

    @property
    def atributos(self):
        print("Número:  {0}".format(self.__numero))
        print("Titular: {0}".format(self.__titular))
        print("Saldo:   {0}".format(self.__saldo))
        print("Limite:  {0}".format(self.__limite))

    @property
    def saldo(self):
        print("O saldo de {0} é: {1}".format(self.__titular, self.__saldo))

    @property
    def limite(self):
        return self.__limite

    def Deposita(self,valor):
        self.__saldo += valor

    def Saca(self, valor):
        self.__saldo -= valor

    def Transfere(self,valor,destino):
        self.__saldo -= valor
        destino.__saldo += valor

    @limite.setter
    def limite(self,valor):
        self.__limite = valor
        print("Limite atualizado para: {0}".format(self.__limite))