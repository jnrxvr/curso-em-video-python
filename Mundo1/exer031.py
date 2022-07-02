# Exercício Python 31:
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

km = int(input('Digite a distância da viagem em Km: '))
preco = 0

if km <= 200:
    preco = km * 0.5
else:
    preco = km * 0.45
print('O valor da passagem para sua viagem de {} Km é de R$ {:.2f}.'.format(km, preco))
