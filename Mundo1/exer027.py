# Exercício Python 27:
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Digite um nome: ').strip().lower()
nNome = nome.split()
print('Primeiro nome: {}' .format(nNome[0]))
print('Segundo nome: {}' .format(nNome[-1]))
