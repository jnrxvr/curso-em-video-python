# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios
# e colocar em uma tupla. Depois disso, mostre a listagem de números gerados
# e também indique o menor e o maior valor que estão na tupla.

from random import randint
x = (randint(1, 100), randint(1, 100), randint(1, 100),
     randint(1, 100), randint(1, 100))
print(f'Valores sorteados: {x}.')
print(f'O maior número da tupla é: {max(x)}.')
print(f'O menor número da tupla é: {min(x)}.')