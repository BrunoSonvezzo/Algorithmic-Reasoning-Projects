''' A tabela progressiva mensal do Imposto de Renda Retido
na Fonte estabelece as seguintes alíquotas (valores e
limites não atualizados):
– de R$ 1.257,13 até R$ 2.512,08,  alíquota de 15%
– acima de R$ 2.512,08,  alíquota de 27,5 %
• Escreva um algoritmo em Python que leia o salário de um
funcionário e calcule o valor do desconto.'''

salario = float(input("Digite o seu salário por favor:"))
while salario < 1257.13:
    print("Isento de imposto, insira outro salário, por favor:")
    salario = float(input())
if salario >= 1257.13 and salario <= 2512.08:
     desconto = salario*0.15
     salario_final = salario-desconto
     print("Seu desconto foi de:R$",round(desconto))
     print("Seu salário com o desconto foi de:R$", round(salario_final))
elif salario > 2512.08:
    desconto = salario*0.275
    print("Seu desconto foi de:R$",round(desconto))
    salario_final = salario - desconto
    print("Seu salário final foi de:R$",round(salario_final))