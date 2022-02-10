'''
Project: Jogo de adivinhação
Company: Alura- Python 3 parte 1: Introdução a nova versão da linguagem
By: Pedro Tiago Bernabé Lomas
Mobile: +55 (12) 98858-5806
LinkedIn: linkedin.com/in/pedro-tiago-bernabé-lomas-6b466194
Create: 2022-02-10
Language: Python
Version: 3.10.2

***** Modified
By:
Date:

By:
Date:

By:
Date:
'''


''' ***** VARIAVEIS '''

# Inteiras
nChute  = 0 # Valor escolhido pelo usuário
nLimite_Maximo = 100 # Maximo valor que o usuario pode chutar
nLimite_Minimo = 1 # Minimo valor que o usuario pode chutar
nNumero_Secreto = 0 # Valor a ser adivinhado
nPontos = 1000 # Pontuacao final do usuario
nPontos_Perdidos = 0
nPontuacao_Final = 0
nReg_1 = 0 # Registrador auxiliar para calculos e armazanamentos rapidos
nRodada = 0 # Rodada atual
nTentativas = 3 # Quantidade de tentativas que o usuario pode ter

# Booleanas
bAcertou = False
bContinuar = True # Garante outra rodada do jogo
bErrou   = False
bFim_De_Jogo = False # Informa que o jogo acabou
bMaior   = False
bMenor   = False
bValor_Fora_Range = False

# Strings
sReg_1 = "" # Registrador auxiliar para calculos e armazanamentos rapidos

''' ***** REGRAS DE NEGOCIO '''
'''
bAcertou = (nChute == nNumero_Secreto)
bErrou   = (nChute != nNumero_Secreto)
bMaior   = (nChute > nNumero_Secreto)
bMenor   = (nChute < nNumero_Secreto)
'''
''' ***** BIBLIOTECAS '''
import random
import os

'''
*********************************
Rotina Main do jogo de adivinhação
*********************************
'''
while (bContinuar):

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")

    nNumero_Secreto = random.randrange(nLimite_Minimo,(nLimite_Maximo+1))
    nPontos_Perdidos = 0

    nReg_1 = 0
    while ((nReg_1 < 1) or (nReg_1 > 3)):
        print("1 - Fácil    = 20 tentativas")
        print("2 - Moderado = 10 tentativas")
        print("3 - Difícil  =  3 tentativas")
        nReg_1 = int(input("Em qual nível de dificuldade você deseja jogar?: "))
        if ((nReg_1 < 1) or (nReg_1 > 3)):
            print("!!!!! Escolha inválida -_-", end="\n\n")

    if (nReg_1 == 1):
        nTentativas = 20
    elif (nReg_1 == 2):
        nTentativas = 10
    elif (nReg_1 == 3):
        nTentativas = 3

    for nRodada in range(1,(nTentativas+1)):

        print("--> Tentativa {0} de {1}".format(nRodada, nTentativas))
        nChute = int(input("Digite um número de {0} à {1}: ".format(nLimite_Minimo, nLimite_Maximo)))
        print()
        print("Você digitou: {0}".format(nChute))

        # Regras de negógio
        bAcertou = (nChute == nNumero_Secreto)
        bErrou   = (nChute != nNumero_Secreto)
        bMaior   = (nChute > nNumero_Secreto)
        bMenor   = (nChute < nNumero_Secreto)
        bValor_Fora_Range = ((nChute < nLimite_Minimo) or (nChute > nLimite_Maximo))

        if (bValor_Fora_Range):
            print("Você deve escolher um valor entre {0} e {1}".format(nLimite_Minimo, nLimite_Maximo))
            continue

        if (bAcertou):
            print("Você acertou :)")
            print("*** CONTRATULATIONS ***", end="\n\n")
            nPontuacao_Final = nPontos - nPontos_Perdidos
            print(f'Sua pontuação final foi de: {nPontuacao_Final}')
            break

        elif (bErrou):
            print("Você errou :/ ", end="\n")

            if (bMaior):
                sReg_1 = "acima"
            elif (bMenor):
                sReg_1 = "abaixo"

            print("O seu número está {} do correto".format(sReg_1), end="\n\n")

            nRodada = nRodada + 1
            nPontos_Perdidos = nPontos_Perdidos + abs(nNumero_Secreto - nChute)

    if (bErrou):
        print("Suas tentativas acabaram :'(")
        print("*** GAME OVER ***", end="\n\n")
        nPontuacao_Final = nPontos - nPontos_Perdidos
        print(f'Sua pontuação final foi de: {nPontuacao_Final}')

    #Jogar novamente
    print("1 - SIMMM :)")
    print("2 - não :(")
    nReg_1 = int(input("Quer jogar de novo?: "))

    if(nReg_1 == 1):
        bContinuar = True

    else:
        bContinuar = False

    os.system('CLS')