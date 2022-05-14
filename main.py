'''Implemente um programa em Python para ler 10 inteiros do teclado. Imprima
cada número lido na tela, desde que o mesmo seja positivo. Dica: você vai
precisar utilizar o while e o if neste exercício'''


print("Mostrando 10 numeros digitados:")
numero = int(input("Insira o número:"))
while numero > 0:
    print(numero)
    numero = int(input("Insira o número:"))
    if numero < 0:
        print("Número inválido")
        continue
while numero > 0:
    print(numero)
    numero = int(input("Insira o número novamente:"))


