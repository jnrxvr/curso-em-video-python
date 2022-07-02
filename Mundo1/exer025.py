#Exercício Python 25:
# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = input('Digite um nome: ').strip().lower()
print('Tem "Silva" no nome? {}' .format('silva' in nome))