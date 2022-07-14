# Exercício Python 56:
# Desenvolva um programa que leia o
# nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho e
# quantas mulheres têm menos de 20 anos.

somaIdades = 0
nomeMaisVelho = ''
menosVinte = 0
maiorIdade = 0

for i in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: '.format(i)))
    idade = int(input('Digite a idade da {}ª pessoa: '.format(i)))
    sexo = str(input('Digite o sexo da {}ª pessoa [Masculino/Feminino]: '.format(i))).lower()
    somaIdades += idade

    if sexo == 'masculino':
        if i == 1:
            maiorIdade = idade
            nomeMaisVelho = nome
        else:
            if idade > maiorIdade:
                maiorIdade = idade
                nomeMaisVelho = nome

    if sexo == 'feminino' and idade < 20:
        menosVinte += 1

mediaIdade = somaIdades / 4
print('----------------------------------')
print('A média de do grupo é de: {} anos.' .format(mediaIdade))
print('O nome do homem mais velho é: {}.'.format(nomeMaisVelho))
print('A quantidade de mulheres com menos de 20 anos é: {}.'.format(menosVinte))
