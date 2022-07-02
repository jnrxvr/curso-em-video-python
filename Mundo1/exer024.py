#Exercício Python 24:
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('Digite a cidade que você nasceu: ').strip().lower()
print('santo' in cidade[0:5])