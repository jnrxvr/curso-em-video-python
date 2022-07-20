# Exercício Python 69:
# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

contMulheresVinte = 0
contMaiorIdade = 0
contHomens = 0
resp = ''
sexo = ''
idade = 0

while True:
    print('***** CADASTRO DE PESSOAS *****')
    idade = int(input('Digite a idade: '))

    sexo = str(input('Digite o sexo: ')).strip().lower()[0]
    while sexo != 'F' and sexo != 'f' and sexo != 'M' and sexo != 'm':      # "while sexo not in 'mf'" tbm funciona
        print('Resposta inválida! Digite F/f ou M/m.')
        sexo = str(input('Digite o sexo: ')).strip().lower()[0]

    resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while resp != 'S' and resp != 's' and resp != 'N' and resp != 'n':
        print('Resposta inválida! Digite S/s ou N/n.')
        resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]

    if idade > 18:
        contMaiorIdade += 1

    if sexo in 'Ff' and idade >= 20:
        contMulheresVinte += 1

    if sexo in 'Mm':
        contHomens += 1

    if resp == 'n':
        break
print('*' * 40)
print(f'Quantidade de pessoas com mais de 18 anos: {contMaiorIdade}.'
      f'\nQuantidade de homens cadastrados: {contHomens}.'
      f'\nQuantidade de mulheres com pelo menos 20 anos de idade: {contMulheresVinte}.')
