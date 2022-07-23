# Escreva um programa que receba um número natural  n n na entrada e imprima  n! n! (fatorial) na saída.

n = int(input("Digite um número para cálculo do fatorial: "))
fat = 1
aux = 0

if n == 0:
    1
else:
    while n != 0:
        fat = fat * n
        aux = aux + fat
        n -= 1
print(fat)