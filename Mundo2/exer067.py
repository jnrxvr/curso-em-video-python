# Exercício Python 67:
# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

num = ''
cont = 0

while True:
    num = int(input('Digite um número para cálculo da tabuada (número negativo para parar): '))
    if num < 0:    # antes do laço de cálculo, para que o laço de cálculo não seja executado se o 'num' for negativo
        break
    while cont <= 10:
        print(f'{num} x {cont} = {num * cont}')
        cont += 1
    print('-----------------------')
    if cont == 11:
        cont = 0

