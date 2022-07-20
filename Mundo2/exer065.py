# Exercício Python 65:
# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e
# qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário
# se ele quer ou não continuar a digitar valores.

cont = 1
media = 0
soma = 0
maior = 0
menor = 0
resp = ''

while resp in 'Ss':
# usar 'in' para que o prog finalize caso o usuário digite "N/n/não/Não" ou seja digitado algum número por acidente

    if cont == 1:  # para a primeira iteração o maior e menor peso serão iguais
        num = int(input('Digite um valor inteiro: '))
        soma = num
        media = num
        maior = num
        menor = num
        cont += 1
        resp = str(input('Deseja continuar [S/N]? ')).strip().lower()[0]
    else:
        num = int(input('Digite um valor inteiro: '))
        soma = soma + num
        media = soma / cont
        cont += 1
        resp = str(input('Deseja continuar [S/N]? ')).strip().lower()[0]
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('***************************')
print('Média: {}'
      '\nMaior valor: {}'
      '\nMenor valor: {}' .format(media, maior, menor))