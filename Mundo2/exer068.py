# Exercício Python 68:
# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randrange
numPC = randrange(0, 10)
somaDedos = 0
escolhaPC = ''
contVit = 0
vencedor = ''

while True:
    escolhaHumano = str(input('Par ou ímpar? Digite sua escolha: ')).strip().lower()
    num = int(input('Digite um número de 1 a 10: '))
    print('*' * 35)
    somaDedos = numPC + num

    if escolhaHumano != 'par' and (num > 10 or num < 0):
        print('Opção inválida! Tente novamente.')
        print('*' * 35)
        somaDedos = 0
        escolhaHumano = str(input('Par ou ímpar? Digite sua escolha: ')).strip().lower()
        num = int(input('Digite um número de 1 a 10: '))
        print('*' * 35)
        somaDedos = numPC + num

    elif escolhaHumano != 'ímpar' and (num > 10 or num < 0):
        print('Opção inválida! Tente novamente.')
        print('*' * 35)
        somaDedos = 0
        escolhaHumano = str(input('Par ou ímpar? Digite sua escolha: ')).strip().lower()
        num = int(input('Digite um número de 0 a 10: '))
        print('*' * 35)
        somaDedos = numPC + num

    if escolhaHumano == 'par':
        escolhaPC = 'ímpar'
    else:
        escolhaPC = 'par'

    if (escolhaHumano == 'par') and (somaDedos % 2 == 0):
        if somaDedos % 2 == 0:
            vencedor = 'par'
        elif somaDedos % 2 == 1:
            vencedor = 'ímpar'
        elif somaDedos == 0:
            vencedor = 'par'

        print('VOCÊ GANHOU!!')
        print(f'Sua escolha: {escolhaHumano}'
              f'\nMinha escolha: {escolhaPC}'
              f'\nSua mão: {num}'
              f'\nMinha mão: {numPC}'
              f'\nSoma dos dedos: {somaDedos}'
              f'\nVence quem escolheu: {vencedor}')
        print('*' * 35)
        contVit += 1

    elif (escolhaHumano == 'ímpar') and (somaDedos % 2 == 1):
        if somaDedos % 2 == 0:
            vencedor = 'par'
        else:
            vencedor = 'ímpar'
        print('VOCÊ GANHOU!!')
        print(f'Sua escolha: {escolhaHumano}'
              f'\nMinha escolha: {escolhaPC}'
              f'\nSua mão: {num}'
              f'\nMinha mão: {numPC}'
              f'\nSoma dos dedos: {somaDedos}'
              f'\nVence quem escolheu: {vencedor}')
        print('*' * 35)
        contVit += 1
    else:
        if somaDedos % 2 == 0:
            vencedor = 'par'
        else:
            vencedor = 'ímpar'
        print('VOCÊ PERDEU!!')
        print(f'Sua escolha: {escolhaHumano}'
              f'\nMinha escolha: {escolhaPC}'
              f'\nSua mão: {num}'
              f'\nMinha mão: {numPC}'
              f'\nSoma dos dedos: {somaDedos}'
              f'\nVence quem escolheu: {vencedor}')
        print('*' * 35)
        break

print(f'Você me venceu {contVit} vezes.')
