# Exercício Python 26:
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

nome = input('Digite um nome: ').strip().lower()
print('Quantas vezes aparece a letra "A" no nome? {} vezes.' .format(nome.count('a')))
print('Em que posição ela aparece na primeira vez? {}ª posição.' .format(nome.find('a')), end='')
print(' (lembre-se que em python o índice da primeira posição é 0)')

print('Em que posição ela aparece pela última vez? {}ª posição.' .format(nome.rfind('a')))
# nesse último print utiliza-se o método 'rfind'
# para que o programa procure a letra 'a' a partir do lado direito