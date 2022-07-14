# Exercício Python 61: Refaça o DESAFIO 51,
# lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('GERADOR DE PA')
primeiro = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite o valor da razão da P.A: '))
termo = primeiro
cont = 1
total = 0
mais = 10   # esse exercício começa com o prog mostrando 10 termos

while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' ')
        termo += razao
        cont += 1
    mais = int(input('\nQuantos termos você quer a mais? '))

print('Progressão finalizada com {} termos mostrados.'.format(total))
