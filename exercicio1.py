"""Construa um algoritmo que calcule a quantidade de latas de tinta
necessárias e o custo para pintar tanques cilíndricos de combustível,
em que são fornecidos a altura e o raio desse cilindro.
• Sabe-se que:
– a lata de tinta custa 50,00 reais;
– cada lata contém 5 litros;
– cada litro de tinta pinta 3 metros quadrados.
• Dados de entrada: altura (H) e raio (R)
• Dados de saída: custo (C)  e quantidade  (QTDE)
• Ajuda:
– custo é dado por quantidade de latas * 50.00;
– quantidade de latas é dada por quantidade total de litros/5;
– quantidade total de litros é dada por área do cilindro/3;
– área do cilindro = área da base + área lateral;
– área da base = (PI * R * R);
– área lateral = altura * comprimento: (2 * PI * R * H);
– sendo que R (raio) e H ( altura) são dados de entrada e PI é uma
constante de valor conhecido: 3.14."""



print("Custos para pintar um cilindro:")
altura = float(input("Insira, por favor, a altura do cilindro que você deseja pintar, em metros:"))
raio = float(input("Insira, por favor, o raio do cilindro, em metros:"))
pi = 3
valor_lata = 50
lata = 15
area = pi*raio*raio*2+2*pi*raio*altura
latas = (area)/lata
custo = latas*valor_lata
if latas <= 1:
    latas = round(latas)
    custo = latas*valor_lata
elif area%lata > 0:
    latas = round(latas)
    custo = latas*valor_lata
    print("Será necessário a compra de mais uma lata de tinta.")
print("Quantidade de latas necessárias:", latas)
print("O custo será de: R$", custo)