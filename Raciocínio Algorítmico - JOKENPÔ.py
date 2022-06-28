from random import randint
from time import sleep
print("Bem vindo ao jogo pedra, papel ou tesoura:")
print("Jogador X Jogador (1);")
print("Jogador X Computador (2);")
print("Computador X Computador (3);")
print("Se deseja encerrar o jogo digite (4);")
exit = 4
while exit != 1:
    escolha = int(input("Escolha seu modo de jogo:"))
#Jogador X Jogador------------------------------------------------------------------------------------------------------
    if(escolha == 1):
        gameover1 = 1
        vitoria1 = 0
        vitoria2 = 0
        empate = 0
        while gameover1 != 4:
            print("Você escolheu o modo: Jogador X jogador")
            jogada1 = int(input("Jogador 1 digite um valor de 0 a 2 sendo, pedra = 0 , papel = 1 , tesoura = 2 "))
            jogada2 = int(input("Jogador 2 digite um valor de 0 a 2 sendo, pedra = 0 , papel = 1 , tesoura = 2 "))
            print("JO")
            sleep(1)
            print("KEN")
            sleep(1)
            print("PÔ!!!")
            if (jogada1 == 0 and jogada2 == 2) or (jogada1 == 2 and jogada2 == 1) or (jogada1 == 1 and jogada2 == 0):
                print("Jogador 1 ganhou!")
                vitoria1 = vitoria1 + 1
            elif (jogada2 == 0 and jogada1 == 2) or (jogada2 == 2 and jogada1 == 1) or (jogada2 == 1 and jogada1 == 0):
                print("Jogador 2 ganhou!")
                vitoria2 = vitoria2 + 1
            elif (jogada1 == 0 and jogada2 == 0) or (jogada1 == 1 and jogada2 == 1) or (jogada1 == 2 and jogada2 == 2):
                print("Empatou!")
                empate = empate + 1
            else:
                print("Comando inválido. Insira um número entre 0 e 2.")
#Sair modo--------------------------------------------------------------------------------------------------------------
            sair = int(input("Se deseja sair do modo de jogo, digite 4. Caso contrário, digite 1:"))
            while sair != 4 and sair != 1:
                print("Comando inválido. Tente novamente com opções entre 0 e 1")
                sair = int(input("Se deseja sair do modo de jogo, digite 4. Caso contrário, digite 1:"))
            if sair == 4:
                break
            elif sair == 1:
                continue

        print("O jogador 1 ganhou:",vitoria1,'\n'"O jogador 2 ganhou:",vitoria2,'\n'"E tiveram: ",empate,"empate(s)"'\n')

#Jogador X Computador---------------------------------------------------------------------------------------------------
    elif(escolha == 2):
        print("Você escolheu o modo: Jogador X Computador")
        gameover2 = 1
        vitoriajogador = 0
        empate = 0
        vitoriaPC = 0
        while gameover2 != 4:
            jogada1 = int(input("Digite um valor de 0 a 2 sendo, pedra = 0 , papel = 1 , tesoura = 2 "))
            computador = randint(0, 2)
            print("JO")
            sleep(1)
            print("KEN")
            sleep(1)
            print("PÔ!!!")
            if (jogada1 == 0 and computador == 2) or (jogada1 == 2 and computador == 1) or (jogada1 == 1 and computador == 0):
                print("Jogador 1 ganhou!")
                print("O computador jogou:",computador)
                vitoriajogador = vitoriajogador + 1
            elif (computador == 0 and jogada1 == 2) or (computador == 2 and jogada1 == 1) or (computador == 1 and jogada1 == 0):
                print("Computador ganhou!")
                print("O computador jogou:",computador)
                vitoriaPC = vitoriaPC + 1
            elif (jogada1 == 0 and computador == 0) or (jogada1 == 1 and computador == 1) or (jogada1 == 2 and computador == 2):
                print("Empatou!")
                print("O computador jogou:",computador)
                empate = empate + 1
            else:
                print("Comando inválido. Insira um número entre 0 e 2.")
#---sair do jogo-------------------------------------------------------------------------------------------------------
            sair = int(input("Se deseja sair do modo de jogo, digite 4. Caso contrário, digite 1:"))
            while sair != 4 and sair != 1:
                print("Comando inválido. Tente novamente com opções 4 e 1")
                sair = int(input("Se deseja sair do modo de jogo, digite 4. Caso contrário, digite 1:"))
            if sair == 4:
                break
            elif sair == 1:
                continue

        print("O jogador 1 ganhou:",vitoriajogador,'\n'"O PC ganhou:",vitoriaPC,'\n'"E tiveram: ",empate,"empate(s)"'\n')

#Computador X Computador------------------------------------------------------------------------------------------------
    elif(escolha == 3):
        gameover3 = 1
        vitoriaPC1 = 0
        vitoriaPC2 = 0
        empatePC = 0
        while gameover3 != 4:
            print("Você escolheu o modo: Computador X Computador")
            print("Pedra = 0, Papel = 1, Tesoura = 2")
            print("JO")
            sleep(1)
            print("KEN")
            sleep(1)
            print("PÔ!!!")
            computador1 = randint(0, 2)
            computador2 = randint(0, 2)
            print("O ComputadorONE jogou", computador1)
            print("O ComputadorTWO jogou", computador2)
            if (computador1 == 0 and computador2 == 2) or (computador1 == 2 and computador2 == 1) or (computador1 == 1 and computador2 == 0):
                print("O computadorONE ganhou !")
                vitoriaPC1 = vitoriaPC1 + 1
            elif (computador2 == 0 and computador1 == 2) or (computador2 == 2 and computador1 == 1) or (computador2 == 1 and computador1 == 0):
                print("O computadorTWO ganhou !")
                vitoriaPC2 = vitoriaPC2 + 1
            elif (computador1 == 0 and computador2 == 0) or (computador1 == 1 and computador2 == 1) or (computador1 == 2 and computador2 == 2):
                print("Empatou!")
                empatePC = empatePC + 1
#----------sair do modo-------------------------------------------------------------------------------------------------------------------------
            sair = int(input("Se deseja sair do modo de jogo, digite 4. Caso contrário, digite 1:"))
            while sair != 4 and sair != 1:
                    print("Comando inválido. Tente novamente com opções 4 e 1")
                    sair = int(input("Se deseja sair do modo de jogo, digite 4. Caso contrário, digite 1:"))
            if sair == 4:
                break
            elif sair == 1:
                continue

        print("O PC1 ganhou:",vitoriaPC1,'\n'"O PC2 ganhou:",vitoriaPC2,'\n'"E tiveram: ",empatePC,"empate(s)"'\n')

    elif escolha  == 4:
        break
    else:
        print("Comando inválido. Escolha opções entre 0 e 4.")