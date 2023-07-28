import os
import time
import forca
import advinhacao

def escolhe_jogo():
    print("################################")
    print("<*****Escolha o seu jogo :)*****>")
    print("################################")

    print("(1) Jogo da Advinhação Numérica \n(2) Jogo da Forca")

    jogo = int(input("Qual Jogo? "))

    if(jogo == 1):
        os.system('cls')
        advinhacao.jogar()
    elif(jogo == 2):
        os.system('cls')
        forca.jogar()
    else:
        print("Selecione um jogo valido!")
        time.sleep(3)
        os.system('cls')

if (__name__ == "__main__"):
    escolhe_jogo() 