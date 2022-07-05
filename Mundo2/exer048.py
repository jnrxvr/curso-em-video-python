# Exercício Python 48: Faça um programa que calcule
# a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.
# extra: conte o total de números somados (contador)

soma = 0
n = 0

for i in range(3, 501, 3):
    if i % 2 == 1:
        soma += i   # acumulador
        n += 1      # contador dos números somadps
print('*********************************************')
print('A soma dos {} valores ímpares, totalizou: {}.'.format(n, soma))