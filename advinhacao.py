import random
import os
import time
import games

def jogar():
    os.system('cls')
    print("################################")
    print("Bem-vindo ao jogo da Advinhação!")
    print("################################")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    #print (numero_secreto)

    print("Qual nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Digite o nível: "))

    if(nivel == 1):
            total_de_tentativas = 10
    elif(nivel == 2):
            total_de_tentativas = 5
    elif(nivel == 3):
            total_de_tentativas = 3
    else:
            print("Nivel invalido")

    for rodada in range(1, total_de_tentativas + 1): 
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        
        chute_str = input("Digite um seu numero entre 1 a 100: ")
        chute = int(chute_str)
        print("Você digitou:", chute)

        if(chute < 1 or chute > 100): 
            print("Você deve digitar somente numeros entre 1 e 100")
            continue
            

        acertou = chute == numero_secreto
        errou_pra_cima = chute > numero_secreto
        errou_pra_baixo = chute < numero_secreto

        if (acertou):
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        elif(errou_pra_cima):
            print("Você errou! Seu chute foi maior que o numero secreto. :/")
        elif(errou_pra_baixo):
            print("Você errou! Seu chute foi menor que o numero secreto. :/")
        
        pontos_perdidos = abs(numero_secreto) - chute
        pontos = pontos - pontos_perdidos

    print("Fim do jogo")
    time.sleep(5)    
    os.system('cls')
    games.escolhe_jogo() 

if(__name__== "__main__"):
    jogar()