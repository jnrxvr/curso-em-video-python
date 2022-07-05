# Exercício Python 52:
# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo.
n = int(input('Digite um número: '))

for i in range(1, n + 1):
    if n % i == 0:
        print('\033[33m', end=' ')
    else:
        print('\033[m', end=' ')
    print('{}' .format(i), end=' ')
