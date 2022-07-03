# Exercício Python 045:
# Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

print('----------------------------------')
opcao = int(input('Escolha sua opção para começar o jogo: '
                  '\n[ 1 ] - PEDRA'
                  '\n[ 2 ] - PAPEL'
                  '\n[ 3 ] - TESOURA'
                  '\nOpção escolhida: '))
n = random.randint(1, 3)
print('='*40)
opcaoComp = ''
opcaoJog = ''

if (1 <= opcao <= 3) and (1 <= n <= 3):
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!')
    sleep(1.5)  # neste caso, serve para dar a ideia de que o computador está pensa, criando uma tensão no jogador
    print('=' * 40)

    if n == 1:
        opcaoComp = 'Pedra'
    elif n == 2:
        opcaoComp = 'Papel'
    else:
        opcaoComp = 'Tesoura'

    if opcao == 1:
        opcaoJog = 'Pedra'
    elif opcao == 2:
        opcaoJog = 'Papel'
    else:
        opcaoJog = 'Tesoura'

    if (opcao == 1 and n == 1) or (opcao == 2 and n == 2) or (opcao == 3 and n == 3):
        print('Houve um empate entre você e o computador!')
        print('Sua jogada: {}.'.format(opcaoJog))
        print('Jogada computador: {}.'.format(opcaoComp))
    elif (opcao == 1 and n == 3) or (opcao == 2 and n == 1) or (opcao == 3 and n == 2):
        print('Parabéns! Você venceu o computador!')
        print('Sua jogada: {}.'.format(opcaoJog))
        print('Jogada computador: {}.'.format(opcaoComp))
    else:
        print('Você perdeu para o computador!')
        print('Sua jogada: {}.'.format(opcaoJog))
        print('Jogada computador: {}.'.format(opcaoComp))
else:
    print('Opção inválida! Reinicie o jogo.')
