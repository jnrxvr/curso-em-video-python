# Exercício Python 67:
# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

# SOLUÇÃO MAIS ELEGANTE

while True:
    num = int(input('Digite um número para cálculo da tabuada (número negativo para parar): '))
    if num < 0: # teste de parada após leitura do número
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')
    print('-' * 30)
print('TABUADA FINALIZADA!')