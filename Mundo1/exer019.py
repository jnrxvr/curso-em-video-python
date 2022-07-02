import random

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')

list = [nome1, nome2, nome3, nome4]

escolha = random.choice(list) # 'choice': uma escolha dentro da lista

print('O(A) aluno(a) escolhido(a) foi: {}.' .format(escolha))

