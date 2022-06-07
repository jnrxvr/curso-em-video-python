# faça um programa que leia um número e mostre seu dobro, triplo e sua raiza quadrada

num = float(input('Digite um número inteiro: '))

dobro = num * 2
triplo = num * 3
raiz_quad = num ** (1/2)

print('O número digitado foi {}, seu dobro é {}, seu triplo é {}, sua raiz quadrada é {:.3f}.'.format(num, dobro, triplo, raiz_quad))