# Exercício Python 63:
# Escreva um programa que leia um número N inteiro qualquer
# e mostre na tela os N primeiros elementos
# de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

print('*** SEQUÊNCIA DE FIBONACCI ***')
termos = int(input('Digite o números de termos da sequência de Fibonacci: '))
cont = 3        # já mostrei os dois primeiros termos, portanto começa do terceiro
t1 = 0
t2 = 1
prox = 0

print('{} {}' .format(t1, t2), end='')

while cont <= termos:
    t3 = t1 + t2
    print(' {}'. format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('\n----- FIM -----')
