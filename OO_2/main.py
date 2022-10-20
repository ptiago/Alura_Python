'''
Project: Orientação a objeto 2
Company: Alura - Python: avançando na linguagem
By: Pedro Tiago Bernabé Lomas
WhatsApp: +55 (12) 98858-5806
LinkedIn: https://www.linkedin.com/in/pedro-lomas/
E-mail: ptiago.lomas@gmail.com
Create: 2022-10-14
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

class Programa:
    def __init__(self,nome,ano):
        self._nome = nome
        self._ano = ano
        self._likes = 0

    # #*** PROPRIEDADES
    def __str__(self):
        return "Nome: {0} \nAno:  {1} \nLikes:{2} \n".format(self._nome,self._ano,self._likes)

    @property
    def nome(self):
        return self._nome

    @property
    def ano(self):
        return self._ano

    @property
    def likes(self):
        return self._likes

    #*** GETTERS

    #*** SETTERS
    @nome.setter
    def nome(self,nome):
        self._nome = nome

    #*** MÉTODOS
    def Inc_Like(self):
        self._likes += 1

class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self._duracao = duracao

    # # *** PROPRIEDADES
    def __str__(self):
        return "Nome: {0} \nAno:  {1} \nDuração: {3} min \nLikes:{2} \n".format(self._nome, self._ano, self._likes,self._duracao)

class Serie(Programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome,ano)
        self._temporadas = temporadas

    # *** PROPRIEDADES
    def __str__(self):
        return "Nome: {0} \nAno:  {1} \nTemporadas: {3} \nLikes:{2} \n".format(self._nome, self._ano, self._likes,self._temporadas)

class PlayList():
    def __init__(self,nome,lista_1):
        self._nome = nome
        self._lista_1 = lista_1

    def __getitem__(self, item):
        return self._lista_1[item]

    def __len__(self):
        return len(self._lista_1)

#Declara objetos
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

#Atribui likes
vingadores.Inc_Like()
vingadores.Inc_Like()
vingadores.Inc_Like()
atlanta.Inc_Like()
atlanta.Inc_Like()

#Filmes e séries
set_1 = [vingadores,atlanta]
set_2 = [demolidor,tmep]

#Playlists
PlayList_1 = PlayList("fds",set_1)

print(vingadores in PlayList_1)

print(len(PlayList_1))

for i in PlayList_1:
    print(i)