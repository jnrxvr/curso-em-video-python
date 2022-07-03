# Exercício Python 42:
# Refaça o DESAFIO 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
print('---------------------------------------')

if a < (b + c) and b < (a + c) and c < (a + b):
    print('É possível formar um triângulo!')
    if a == b == c:
        print('Os segmentos formam um triângulo equilátero!')
    elif a == b or b == c or c == a:
        print('Os segmentos formam um triângulo isósceles!')
    else:
        print('Os segmentos formam um triângulo escaleno!')
else:
    print('Não é possível formar um triângulo!')