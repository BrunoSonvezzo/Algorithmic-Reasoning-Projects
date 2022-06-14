CoordenadasX = 20#quantidade de linhas
CoordenadasY = 20#quantidade de colunas
porta_avioes = [3,4]#lista que define quantidade de porta-aviões e quantidade de peças que ele possui
cruzador = [4,3]#lista que define quantidade de porta-aviões e quantidade de peças que ele possui
fragata = [5,2]#lista que define quantidade de porta-aviões e quantidade de peças que ele possui
intervalo = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']#lista com o intervalo de posições que são aceitas, para depois converter em inteiro
def gerador_Tabuleiro():
    global tabuleiro
    tabuleiro = [0] * CoordenadasX
    for x in range(CoordenadasX):
        tabuleiro[x] = ['0'] * CoordenadasY
def visualizar_Tabuleiro():
    for x in range(CoordenadasX):
        print(tabuleiro[x])
def posicionar_pecas():
    quant_navios = 12
    cont_portaAvioes = 0#contador de porta-aviões posicionados
    cont_cruzador = 0#contador de cruzadores posicionados
    cont_fragata = 0#contador de fragatas posicionadas
    print("Modelos de Navios\n","Porta-Aviões (Você possui 3, e cada uma possui 4 partes)\n","Cruzador (Você possui 4, e cada um possui 3 partes)\n","Fragata (Você possui 5 e cada um possui 2 partes)\n")
    while quant_navios > 0:#laço que só se encerra ao posicionar todos as navios
        print("Identificação das embarcações \n","P - Porta-Aviões.\n","C - Cruzador.\n","F - Fragata.\n")
        while True:#recebe e valida o tipo da embarcação
            print(f"\nJá posicionou;\n Porta Avião: {cont_portaAvioes}\n Cruzador: {cont_cruzador}\n Fragata: {cont_fragata}", end="\n\n")
            id_navio = input("Dê a identificação do návio: ")
            if id_navio == "P":#verifica se é um porta-aviões
                quant_Pecas = porta_avioes[1]
                cont_portaAvioes += 1#contador de quantos foram posicionados
                if cont_portaAvioes > porta_avioes[0]:#testa se já foi utilizado a quantidade máxima de embarcações
                    print('Quantidade de Porta Aviões atingida!')
                    continue
                else:
                    break
            elif id_navio == "C":#verifica se é um cruzador
                quant_Pecas = cruzador[1]
                cont_cruzador += 1#contador de quantos foram posicionados
                if cont_cruzador > cruzador[0]:#testa se já foi utilizado a quantidade máxima de embarcações
                    print('Quantidade de Cruzador atingida!')
                    continue
                else:
                    break
            elif id_navio == "F":#verifica se é uma fragata
                quant_Pecas = fragata[1]
                cont_fragata += 1#contador de quantos foram posicionados
                if cont_fragata > fragata[0]:#testa se já foi utilizado a quantidade máxima de embarcações
                    print('Quantidade de Fragata atinigda!')
                    continue
                else:
                    break
            else:
                print("Modelo inexistente. Tente novamente! ")
                continue
        limiteY = 20 - quant_Pecas
        print("ATENÇÃO!!")
        print(f"As posições de X variam de 0 até 19, e os de Y variam de 0 até {limiteY}")
        while True:#pergunta as coordenadas, preenche a matriz e valida os dados
            while True:#valida coordenada X
                entrada_X = input("Dê as coordenadas de X que gostaria de dispor a peça: ")
                if entrada_X in intervalo:#testa se a entrada está dentro de uma lista previamente definida, se sim, converte ela para inteiro e passa para a variavel entrada_X
                  entrada_X = int(entrada_X)
                  break
                else:
                  print('Entrada inválida ou Coordenada inexistente. Tente novamente!')
                  continue
            while True:#valida coordenada Y:
                entrada_Y = input("Dê as coordenadas de Y que gostaria de dispor a peça: ")
                if entrada_Y in intervalo:#testa se a entrada está dentro de uma lista previamente definida, se sim, converte ela para inteiro e passa para a variavel entrada_Y
                  entrada_Y = int(entrada_Y)
                  if entrada_Y <= limiteY:#testa se a embarcação cabe no tabuleiro, para evitar erro de indexação
                    break
                  else:
                    print("Espaços insuficientes. Tente outra posição!")
                    continue
                else:
                  print('Entrada inválida ou Coordenada inexistente. Tente novamente!')
                  continue
            for verifica in range(quant_Pecas):#testa se as coordenadas estão livres
                if tabuleiro[entrada_X][entrada_Y+verifica] != '0':
                    print(f"Posição [{entrada_X}][{entrada_Y+verifica}] já ocupada por outra embarcação. Tente outra!")
                    ocupada = True
                    break
                else:
                    ocupada = False
            if ocupada:#verifica se todas as posições testadas estão ocupadas ou não, se True, pergunta novas coordernadas
                continue
            else:#se não, preenche o tabuleiro
                for pecas in range(quant_Pecas):#preenche o tabuleiro
                    tabuleiro[entrada_X][entrada_Y+pecas] = id_navio
                break
        visualizar_Tabuleiro()
        quant_navios -= 1
def valida_pontos(tentativa_X,tentativa_Y,partes):#pega a posição do tiro e a quantidade de peças do possivel alvo, definida na chamada da função
  valido = None#cria a variavel valido para não dar unbound error
  if tentativa_Y+partes == 19 or tentativa_Y == 0:#testa se a posição está no extremo 0 ou se a posição + peças do possivel alvo vão até o final da coluna
    for indices in range(1,partes+1):#testa todas as possíveis posições do alvo para a direita
      if tabuleiro[tentativa_X][tentativa_Y+indices] == 'X':
        valido = True
      else:
        valido = False
        break
  elif tentativa_Y-partes == 0 or tentativa_Y == 19:#testa se a posição está no extremo 19 ou se a posição + peças do possivel alvo vão até o começo da coluna
     for indices in range(1,partes+1):#testa todas as possíveis posições do alvo para a esquerda
          if tabuleiro[tentativa_X][tentativa_Y-indices] == 'X':
            valido = True
          else:
            valido = False
            break
  else:# testa todas as possíveis posições tanto para direita como para a esquerda, pois, não está em nenhum extremo
    for indices in range(1,partes+1):
      if tabuleiro[tentativa_X][tentativa_Y+indices] == 'X':
        valido = True
      else:
        valido = False
        break
    for indices in range(1,partes+1):
      if tabuleiro[tentativa_X][tentativa_Y-indices] == 'X':
        valido = True
      else:
        valido = False
        break
  if valido == True:
    return True
  else:
    return False
def tentativa():
    pontuacao = 0
    cont_partesRestantes = 0
    for x in range(CoordenadasX):#percorre a matriz(tabuleiro) e conta quantas peças tem dispostas no tabuleiro.
        for y in range(CoordenadasY):
            if tabuleiro[x][y] != '0':
                cont_partesRestantes += 1
    print("As embarcações estão dispostas no tabuleiro, as coordenadas começam em [0,0] e vão até [19,19], onde X é a linha e Y é a coluna.\n Naufrague todas as embarcações para sair dessa batalha vitorioso!\n ou abandone a batalha no meio como um fujão...")
    while cont_partesRestantes != 0:#laço que só se encerra quando todas as embarcações forem naufragadas
        while True:#valida a entrada da coordenada de x
            tentativa_X = input("Dê a coordenada de X do alvo: ")
            if tentativa_X in intervalo:#testa se a entrada está dentro de uma lista previamente definida, se sim, converte ela para inteiro e passa para a variavel tentativa_X
              tentativa_X = int(tentativa_X)
              break
            else:
              print('Entrada inválida ou Coordenada inexistente. Tente novamente!')
              continue
        while True:#valida a entrada da coordenada de y
            tentativa_Y = input("Dê a coordenada de Y do alvo: ")
            if tentativa_Y in intervalo:#testa se a entrada está dentro de uma lista previamente definida, se sim, converte ela para inteiro e passa para a variavel tentativa_Y
              tentativa_Y = int(tentativa_Y)
              break
            else:
              print('Entrada inválida ou Coordenada inexistente. Tente novamente!')
              continue
        print('-'*100)
        if tabuleiro[tentativa_X][tentativa_Y] != '0':#verifica se a posição possui alguma embarcação
            if tabuleiro[tentativa_X][tentativa_Y] == 'P':#verifica se é um porta-aviões
                print("Fogo! Você acertou um Porta-Aviões.\nPara pontuar, é preciso atingir todas as partes.")
                print('#'*100)
                tabuleiro[tentativa_X][tentativa_Y] = 'X'#troca a identificação do navio por um X para marcar que foi atingido
                alvo_atingido = True
                if valida_pontos(tentativa_X,tentativa_Y,3):#chama a função que verifica se o alvo foi completamente abatido pelos extremos
                    print('Você naufragou um Porta-Aviões.\nGanhou 30 pontos!')
                    print('#'*100)
                    pontuacao += 30
                elif ((tabuleiro[tentativa_X][tentativa_Y-1] == 'X' and tabuleiro[tentativa_X][tentativa_Y+1] == 'X' and tabuleiro[tentativa_X][tentativa_Y+2] == 'X') or (tabuleiro[tentativa_X][tentativa_Y+1] == 'X' and tabuleiro[tentativa_X][tentativa_Y-1] == 'X' and tabuleiro[tentativa_X][tentativa_Y-2] == 'X')):#verifica se o alvo foi abatido pelo meio
                  print('Você naufragou um Porta-Aviões.\nGanhou 30 pontos!')
                  print('#'*100)
                  pontuacao += 30
            elif tabuleiro[tentativa_X][tentativa_Y] == 'C':#verifica se é um cruzador
                print("Fogo! Você acertou um Cruzador.\nPara pontuar, é preciso atingir todas as partes.")
                print('#'*100)
                tabuleiro[tentativa_X][tentativa_Y] = 'X'#troca a identificação do navio por um X para marcar que foi atingido
                alvo_atingido = True
                if valida_pontos(tentativa_X,tentativa_Y,2):#chama a função que verifica se o alvo foi completamente abatido pelos extremos
                  print('Você naufragou um Cruzador.\nGanhou 20 pontos!')
                  print('#'*100)
                  pontuacao += 20
                elif ((tabuleiro[tentativa_X][tentativa_Y-1] == 'X' and tabuleiro[tentativa_X][tentativa_Y+1] == 'X' )):#verifica se o alvo foi abatido pelo meio
                  print('Você naufragou um Cruzador.\nGanhou 20 pontos!')
                  print('#'*100)
                  pontuacao += 20
            elif tabuleiro[tentativa_X][tentativa_Y] == 'F':#verifica se é uma fragata
                print("Fogo! Você acertou uma Fragata.\nPara pontuar, é preciso atingir todas as partes.")
                print('#'*100)
                tabuleiro[tentativa_X][tentativa_Y] = 'X'#troca a identificação do navio por um X para marcar que foi atingido
                alvo_atingido = True
                if valida_pontos(tentativa_X,tentativa_Y,1):#chama a função que verifica se o alvo foi completamente abatido pelos extremos
                  print('Você naufragou uma Fragata.\nGanhou 10 pontos!')
                  print('#'*100)
                  pontuacao += 10
            else:# se não entrar em nenhum dos ifs, significa que é uma posição já atingida, não pontua, nem perde
                print("Parte do návio já atingida.\nVocê não perde ponto, mas também não pontua!")
                print('#'*100)
                continue
        else:# se não for nenhuma embarcação, nem posição já atingida, significa que errou, portanto, perde 1 ponto do total, se o total for 0, não perde ponto.
            print("Água! Você perdeu 1 ponto.")
            alvo_atingido = False
            pontuacao -= 1
        if pontuacao < 0:#se o total for 0, não perde ponto.
          pontuacao = 0
        sair = input(f"Sua pontuação é |{pontuacao}|\nPara continuar a jogar, pressione |Enter|\nPara fechar o jogo, digite |sair|")#pergunta se o usuário quer sair do jogo
        print('-'*100)
        if sair == "sair":
          exit()#função que fecha um programa python
        else:
          if alvo_atingido:
              cont_partesRestantes -= 1
              continue
          else:
              cont_partesRestantes = cont_partesRestantes
              continue
    print("Todas as embarcações foram atingidas!")
def main():
    print("Bem-vindo ao Batalha Naval! Aqui veremos seu desempenho em guerras marítimas!",end="\n\n")
    gerador_Tabuleiro()
    posicionar_pecas()
    print('\n'*200)
    tentativa()
    visualizar_Tabuleiro()
main()