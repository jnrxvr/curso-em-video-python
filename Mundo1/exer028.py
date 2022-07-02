# Exercício Python 28:
# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

print('----------------------------------')
num = int(input('Digite um número entre 0 e 5 para começar o jogo: '))

n = random.randint(0, 5)
print('PROCESSANDO...')
sleep(3) # neste caso, serve para dar a ideia de que o computador está pensa, criando uma tensão no jogador
if num != n:
    print('----------------------------------')
    print('Você perdeu! Tente outra vez.')
    print('O número escolhido pelo computador foi: {}' .format(n))
else:
    print('----------------------------------')
    print('Você venceu! Parabéns!')

print('------------FIM DE JOGO-----------')

