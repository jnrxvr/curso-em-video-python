# Exercício Python 64:
# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados
# e qual foi a soma entre eles (desconsiderando o flag).

num = int(input('Digite um número inteiro: '))
total = 0
soma = num

while num != 999:
    print('999 - para encerrar o programa.')
    total += 1
    soma = soma + num
    num = int(input('Digite um número inteiro: '))

# Coloca-se o comando no final para que o 999 não seja somado. Isso fará com que o bloco não seja executado quando 999
# executado, partindo direto para a linha final

print('O total de números digitados foram {} e o somatório total foi de {}.'.format(total, soma))
