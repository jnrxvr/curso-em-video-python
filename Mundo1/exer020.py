import random

nome1 = input('Digite o primeiro nome: ')
nome2 = input('Digite o segundo nome: ')
nome3 = input('Digite o terceiro nome: ')
nome4 = input('Digite o quarto nome: ')

list = [nome1, nome2, nome3, nome4]

random.shuffle(list) # como não retorna nada faz-se direto, sem atribuir a uma variável

print('A ordem de apresentação é: {}.' .format(list))
