# Exercício Python 35:
# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
print('---------------------------------------')

if a < (b + c) and b < (a + c) and c < (a + b):
    print('É possível formar um triângulo!')
else:
    print('Não é possível formar um triângulo!')
