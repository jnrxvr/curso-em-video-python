# faça um programa que leia um número inteiro e mostre na tela seu antecessor e seu sucessor

num = int(input('Digite um número inteiro: '))
ant = num - 1
suc = num + 1

print('O número digitado foi {}, seu antecessor é {} e o sucessor é {}.'.format(num, ant, suc))