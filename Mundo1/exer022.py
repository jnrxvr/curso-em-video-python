# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao to do (sem considerar espaços).
#- Quantas letras tem o primeiro nome.

# strip() - elimina espaços desnecessários à direita e à esquerda
nome = str(input('Digite o seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())

# para contabilizar o total de letras sem considerar os espaços
# basta subtrair o números de espaços que aparecem (nome.count(' '))
# na string do comprimento total da string (len(name))

print(len(nome) - nome.count(' ')) # nome.count(' ') - contará os espaços no meio da string

name = nome.split() # fatiar o nome em uma lista ex.: ['Junior', 'do', 'Nascimento', 'Xavier']
print(len(name[0]))