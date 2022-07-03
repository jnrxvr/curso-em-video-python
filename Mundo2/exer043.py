# Exercício Python 043:
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e
# mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

from math import pow
massa = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (m): '))
imc = massa / pow(altura, 2)

if imc < 18.5: # 'imc < 18.5' pode ser feito desse jeito tbm
    print('-------------------------------------------------------------------')
    print('Voce está abaixo do peso ideal! Procure um médico ou nutricionista.')
elif imc <= 25:
    print('-------------------------------------------------------------------')
    print('Parabéns! Você está no seu peso ideal!')
elif imc <= 30:
    print('-------------------------------------------------------------------')
    print('Voce está com sobrepeso! Procure um médico ou nutricionista.')
elif imc <= 40:
    print('-------------------------------------------------------------------')
    print('Voce está com obesidade! Procure imediatamente um médico ou nutricionista.')
else:
    print('-------------------------------------------------------------------------------------')
    print('ATENÇÃO!! Voce está com obesidade mórbida! ')
    print('Procure imediatamente um médico ou nutricionista.')
