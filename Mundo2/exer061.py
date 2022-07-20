# Exercício Python 61: Refaça o DESAFIO 51,
# lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('GERADOR DE PA')
primeiro = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite o valor da razão da P.A: '))
termo = primeiro
cont = 10

while cont > 0:
    print(termo, end=' ')
    termo += razao
    cont -= 1


