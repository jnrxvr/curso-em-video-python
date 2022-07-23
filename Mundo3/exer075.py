# Exercício Python 075:
# Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# adicionando os elementos em uma tupla
num = (int(input('Digite o 1º número inteiro: ')), int(input('Digite o 2º número inteiro: ')),
       int(input('Digite o 3º número inteiro: ')), int(input('Digite o 4º número inteiro: ')))
print('=*' * 40)

print(f'Número de vezes que o número 9 apareceu: {num.count(9)} vezes.')
if 3 in num:
    print(f'Posição em que o primeiro valor 3 foi digitado: {num.index(3)} posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares digitados foram: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')

