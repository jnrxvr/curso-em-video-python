# Exercício Python 55:
# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: ' .format(p)))
    if p == 1:      # para a primeira iteração o maior e menor peso serão iguais
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('---------------')
print('Maior peso: {} Kg.' .format(maior))
print('Menor peso: {} Kg.' .format(menor))
