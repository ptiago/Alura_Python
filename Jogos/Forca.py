'''
Project: Jogo da Forca
Company: Alura - Python: avançando na linguagem
By: Pedro Tiago Bernabé Lomas
WhatsApp: +55 (12) 98858-5806
LinkedIn: https://www.linkedin.com/in/pedro-lomas/
Create: 2022-02-10
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

# Inteiras


# Booleanas
bAcertou  = False
bEnforcou = False

# Strings
sChute = ""
sPalavra_Secreta = ""
sReg_1 = "" # Registrador auxiliar para calculos e armazanamentos rapidos

''' ***** REGRAS DE NEGOCIO ***** '''



''' ***** BIBLIOTECAS ***** '''


'''
*********************************
MAIN
*********************************
'''
def Main():
    print("**************************")
    print("Bem-vindo ao jogo da Forca")
    print("**************************")

    #Reseta variaveis
    bAcertou  = False
    bEnforcou = False

    sPalavra_Secreta = "Banana"

    while (not bEnforcou and not bAcertou):

        sChute = input("Digite uma letra")

        print("jogando...")


    print("GAME OVER")

if(__name__ == "__main__"):
    Main()