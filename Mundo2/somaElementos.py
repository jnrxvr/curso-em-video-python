# Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída

elementos = int(input("Digite o número de elementos da soma: "))

soma = 0
valor = 1

while elementos != 0:
    valor = int(input("Digite um número a ser somado: "))
    soma = soma + valor
    elementos -= 1

print("A soma dos", elementos, "elementos é igual a: ", soma)
