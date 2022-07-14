# Exercício Python 54:
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores.

from datetime import date

maiorDeIdade = 0
menorDeIdade = 0
atual = date.today().year

for i in range(1, 8):  # 1 a 8 pra ir da primeira até a sétima pessoa e ficar melhor estéticamente
    anoNasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i)))
    idade = atual - anoNasc
    if idade >= 18:
        maiorDeIdade += 1
    else:
        menorDeIdade += 1
print('---------------------------------------')
print('Número de pessoas maiores de idade: {}.' .format(maiorDeIdade))
print('Número de pessoas menores de idade: {}.' .format(menorDeIdade))
