#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

from datetime import date

anoNascimento = int(input('Digite o ano de nascimento do(a) atleta: '))
idade = date.today().year - anoNascimento

if idade <= 9:
    print('Idade do(a) atleta: {} anos.' . format(idade))
    print('Categoria: MIRIM!')

elif 9 < idade <= 14: # poderia ser apenas 'idade <= 14' (não coloquei pois quero deixar o código mais compreensivo)
    print('Idade do(a) atleta: {} anos.'.format(idade))
    print('Categoria: INFANTIL!')

elif 14 < idade <= 19: # poderia ser apenas 'idade <= 19' (não coloquei pois quero deixar o código mais compreensivo)
    print('Idade do(a) atleta: {} anos.'.format(idade))
    print('Categoria: JÚNIOR!')

elif 19 < idade <= 25: # poderia ser apenas 'idade <= 25' (não coloquei pois quero deixar o código mais compreensivo)
    print('Idade do(a) atleta: {} anos.'.format(idade))
    print('Categoria: SÊNIOR!')

else:
    print('Idade do(a) atleta: {} anos.'.format(idade))
    print('CATEGORIA: MASTER!')

