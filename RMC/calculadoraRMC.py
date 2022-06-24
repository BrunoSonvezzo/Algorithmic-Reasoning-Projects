import math
import matplotlib.pyplot as plt
import numpy as np
import time
def calcular_raizes(a,b,c):
  global raizes
  delta = ((b**2)-(4*a*c))
  if delta < 0:
    delta = ((b**2)-(4*a*c))
    delta = round(math.sqrt(delta*-1),2)
    x1 = f'-{b}+{delta}i/2*{a}'
    x2 = f'-{b}-{delta}i)2*{a}'
    raizes = [x1,x2,1j]
    print(f'Raíz complexa [{x1} , {x2}]')
    return True
  elif delta > 0:
    delta = math.sqrt((b**2)-(4*a*c))
    x1 = round((-b+delta)/2*a,2)
    x2 = round((-b-delta)/2*a,2)
    raizes = [x1,x2,0.0]
    print(f'Raízes reais [{x1},{x2}]')
    return True
  else: 
    x = round(-b/2*a,2)
    raizes = [x,0,0.0]
    print(f'Raiz única [{x}]')
    return True
def calcular_func_pedido(x,a,b,c):
  y = a*x**2+b*x+c
  print(f'f({x}) = {y}')
def calcular_vertice(a,b,c):
  delta = b**2-(4*a*c)
  vertice = [(-b/2*a),(-delta/4*a)]
  if a > 0:
    print(f"Os pontos do vertice minimo são {vertice}.")
  elif a < 0:
    print(f"Os pontos do vertice maximo são {vertice}.")
  return vertice
def plot_funcSegundo(a,b,c):
      if type(raizes[2]) == complex:
        print("\nRaiz complexa")
      elif type(raizes[0]) == float:
        eixo_x = []
        eixo_y = []
        variacao = abs(raizes[0] - raizes[1])
        if variacao < 3:
          variacao = 3
          print(variacao)
        for x in np.arange(raizes[0] - variacao, raizes[1] + variacao, 0.01):
            y = a * (x ** 2 ) + b * (x) + c
            eixo_x.append(x)
            eixo_y.append(y)
        plt.plot(eixo_x,eixo_y,color="blue")
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        plt.show()
def verificar_existencia_func_exp(a,b):
  if a > (1/2) and a != 1:
    print('\nA função existe')
    return True
  else: 
    print('\nA função não existe')
    return False
def verificar_inclinacao(a,b):
  if a > (3/2):
    inclinacao = 'crescente'
  elif a < (3/2) and a > (1/2):
    inclinacao = 'decrescente'
  print(f'\nA função é {inclinacao}')
def calcular_func_exp(a,b,x):
  y = b+(a**x)
  print(f'\nf({x}) = {y}')
def plot_func_exp(a,b):
    vetorx = np.arange(-7,7,0.1)
    y = lambda x: b + a ** x
    vetorY = []
    for x in vetorx:
        vetorY.append(y(x))
    fig = plt.figure(figsize=(5, 5))
    plt.plot(vetorx,vetorY, label='Funcao Exponencial', color='g')
    plt.title('f(x) - a*x')
    plt.xlabel('eixo x')
    plt.ylabel('eixo y')
    plt.legend()
    plt.grid(True, which='both')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()
def gerar_matriz(x,y):
  global matriz
  matriz = x * [0]
  for linha in range(x):
    matriz[linha] = [0] * y
  for linha in range(x):
    for coluna in range(y):
      while True:
        try:
          matriz[linha][coluna] = float(input(f"Digite o valor da célula[{linha},{coluna}]: "))
        except ValueError or TypeError:
          print('Digite inteiros válidos!')
          continue
        else:
          break
  print(f'\nMatriz A {x}x{y}')
  for linha in range(x):
    print(matriz[linha])
  print()
  return matriz
def calcular_determinante_matriz(x1,y1):
  if x1 == y1:
    if (x1 == 2):
      for i in range(x1):
        print(matriz[i])
      soma_diagonalPrincipal = 0
      for diagonalE in range(x1):    
          soma_diagonalPrincipal = matriz[diagonalE][diagonalE] + soma_diagonalPrincipal
      soma_diagonalSecundaria = 0
      inversa = 0
      for diagonalD in range(x1-1,-1,-1):
          soma_diagonalSecundaria = matriz[inversa][diagonalD] + soma_diagonalSecundaria
          inversa += 1
      determinanteMatriz = soma_diagonalPrincipal - soma_diagonalSecundaria
      print(f"\nDeterminante(mat) = {determinanteMatriz}")
    elif x1 == 3:    
      soma_diagonalPrincipal  = matriz[0][0] * matriz[1][1] * matriz[2][2] + matriz[0][1] * matriz[1][2] * matriz[2][0] + matriz[0][2] * matriz[1][0] * matriz[2][1]
      soma_diagonalSecundaria = matriz[2][0] * matriz[1][1] * matriz[0][2] + matriz[2][1] * matriz[1][2] * matriz[0][0] + matriz[2][2] * matriz[1][0] * matriz[0][1]            
      print(f"\nSomaDiagPrinc = {soma_diagonalPrincipal} - SomaDiagSecun = {soma_diagonalSecundaria}")
      determinanteMatriz = soma_diagonalPrincipal - soma_diagonalSecundaria 
      print(f"\nDeterminante(mat) = {determinanteMatriz}") 
  else: 
    print('\nMatriz não é quadrada')
def multiplicar_matriz(matriz,x1,y1):
  while True:
    try:
      x2 = int(input('Digite o número de linhas: '))
      y2= int(input('Digite o número de colunas: '))
    except:
      print('Digite inteiros válidos!')
      continue
    else:
      if y1 == x2:
        matriz2 = [0] * x1
        for linha in range(x1):# cria matriz 2
          matriz2[linha] = [0] * y2
        for linha in range(x2):#preencher a matriz 2
          for coluna in range(y2):
            while True:
              try:
                matriz2[linha][coluna] = float(input(f"Digite o valor da célula[{linha},{coluna}]: "))
              except ValueError or TypeError or IndexError:
                print('Digite inteiros válidos!')
                continue
              else:
                break
        print(f'\nMatriz B {x2}x{y2}')
        for i in range(x1):
          print(matriz2[i])
        matriz3 = [0] * x1
        for linha in range(x1):#cria matriz 3
          matriz3[linha] = [0] * y2
        for linha in range(x1):
          for coluna in range(y2):
            acumula = 0
            for i in range(y1):
              acumula+=matriz[linha][i]*matriz2[i][coluna]
            matriz3[linha][coluna]=acumula
        print(f'\nMatrizA {x1}x{y1} x MatrizB {x2}x{y2} = MatrizC {x1}x{y2}')    
        for i in range(x1):
          print(matriz3[i])
      else:
        print('\nMultiplicação impossível.')
      break
def matriz_transposta(matriz,x,y):
  transposta = []
  transposta = y * [0]
  for linha in range(y):
    transposta[linha] =  x * [0]
  for linha in range(y):
        for coluna in range(x):
              transposta[linha][coluna] = matriz[coluna][linha]
  for i in range(y):
        print(transposta[i])
def menu():
  print('-'*50)
  print("\nCalculadora RMC\n Operações:\n 1 - Funções do 2º Grau\n 2 - Funções Exponenciais\n 3 - Matrizes \n 0 - Para fechar o programa")
  operacao = input("\nQual a operação desejada: ")
  if operacao == '1':
    print("\nDigite o valor dos coeficientes da função.")
    while True:
      try:
        a = float(input('A: '))
        b = float(input('B: '))
        c = float(input('C: '))
      except ValueError:
        print("Digite inteiros válidos")
        continue
      else:
        break
    verifica_raiz = 0
    while True:
      print("\nOperações das Função do 2º\n Opções\n 1 - Calcular Raízes \n 2 - Calcular função de x \n 3 - Calcular vértice \n 4 - Gerar gráfico da função(calcule as raízes primeiro) \n 0 - Voltar para o menu")
      opcoes = input('\nQual opção deseja fazer: ')
      if opcoes == '1':
        calcular_raizes(a,b,c)
        verifica_raiz += 1
        time.sleep(2)
        print('-'*50)
      elif opcoes == '2':
        x = float(input("\nX: "))
        calcular_func_pedido(x,a,b,c)
        time.sleep(2)
        print('-'*50)
      elif opcoes == '3':
        calcular_vertice(a,b,c)
        time.sleep(2)
        print('-'*50)
      elif opcoes == '4':
        calcular_raizes(a,b,c)   
        plot_funcSegundo(a,b,c)
      elif opcoes == '0':
        menu()
      else:
        print("\nOpção inválida. Tente novamente!")
      coef = input('\nSe deseja manter os coeficientes, pressione Enter\ncaso queira mudá-los, digite 1.')
      if coef == '1':
        while True:
          try:
            a = float(input('A: '))
            b = float(input('B: '))
            c = float(input('C: '))
          except ValueError:
            print("Digite inteiros válidos")
            continue
          else:
            break
  elif operacao == '2':
    print("\nDigite o valor dos coeficientes da função.")
    while True:
      try:
        a = float(input('A: '))
        b = float(input('B: '))
      except ValueError:
        print("Digite inteiros válidos")
        continue
      else:
        break
    while True:
      existencia = verificar_existencia_func_exp(a,b) 
      if existencia:
        print("\nOperações de Função exponencial\n Opções\n 1 - Verificar se a função é crescente ou decrescente \n 2 - Calcular função de x \n 3 - Gerar gráfico da função\n 0 - Voltar para o menu")
        opcoes = input('\nQual opção deseja fazer: ')
        if opcoes == '1':
          verificar_inclinacao(a,b)
          time.sleep(2)
          print('-'*50)
        elif opcoes == '2':
          while True:
            try:
              x = float(input("\nX: "))
            except ValueError:
              print('Digite inteiros válidos.')
              continue
            else:
              break
          calcular_func_exp(a,b,x)
          time.sleep(2)
          print('-'*50)
        elif opcoes == '3':
          plot_func_exp(a,b)
          print()
        elif opcoes == '0':
          print('-'*50)
          menu()
        else:
          print("\nOpção inválida. Tente novamente!")
      coef = input('\nSe deseja manter os coeficientes, pressione Enter\ncaso queira mudá-los, digite 1.')
      if coef == '1':
        while True:
          try:
            a = float(input('A: '))
            b = float(input('B: '))
          except ValueError:
            print("Digite inteiros válidos")
            continue
          else:
            break      
  elif operacao == '3':
    while True:
      try:
        x1 = int(input("Digite o número de linhas: "))
        y1 = int(input("Digite o número de colunas: "))
      except ValueError:
        print("Digite inteiros válidos")
        continue
      else:
        break
    gerar_matriz(x1,y1)     
    while True:
      print("\nOperações de Matrizes\n Opções \n 1 - Calcular determinante \n 2 - Multiplicação de matriz \n 3 - Matriz Transposta \n 0 - Voltar para o menu ")
      opcoes = input('\nQual opção deseja fazer: ')
      if opcoes == '1':
        calcular_determinante_matriz(x1,y1)
      elif opcoes == '2':
        multiplicar_matriz(matriz,x1,y1)
      elif opcoes == '3':
        matriz_transposta(matriz,x1, y1)
      elif opcoes == '0':
        menu()
      else:
        print("\nOpção inválida.Tente novamente!")
      coef = input('\nSe deseja manter os coeficientes, pressione Enter\ncaso queira mudá-los, digite 1.')
      if coef == '1':
        while True:
          try:
            x1 = int(input("Digite o número de linhas: "))
            y1 = int(input("Digite o número de colunas: "))
          except ValueError or TypeError:
            print("Digite inteiros válidos")
            continue
          else:
            break
        gerar_matriz(x1,y1)
  elif operacao == '0':
    print('Fechando...')
    time.sleep(1.5)
    exit()
  else:
    print("\nEntrada inválida")
    menu()
try:
  menu()
except:
  print('Culpa do usuário!')