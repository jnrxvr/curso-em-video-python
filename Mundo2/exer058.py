# Exercício Python 58:
# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('----------------------------------')
num = int(input('Digite um número entre 0 e 10 para começar o jogo: '))

n = randint(0, 10)
cont = 0

while num != n:
    num = int(input('ERROOOOU! Tente novamente: '))
    cont += 1
    if num < n:
        print('Digite um número maior.')
    elif num > n:
        print('Digite um número menor.')

print('----------------------------------')
print('Foram necessárias {} tentativas para você me vencer.'.format(cont + 1))
print('------------FIM DE JOGO-----------')