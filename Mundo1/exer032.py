# Exercício Python 32:
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

ano = int(input('Qual o ano deseja analisar? Digite 0 para analisar o ano atual. '))
if ano == 0:
    ano = date.today().year
# ano bissexto tem que ser divisível por e não pode ser múltiplo de 100, exceto os anos que são múltiplos de 400
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('A ano de {} é bissexto.' .format(ano))
else:
    print('A ano de {} não é bissexto.'.format(ano))
