# Exercício Python 57:
# Faça um programa que leia o sexo de uma pessoa,
# mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0] # pega a primeira letra mesmo que digite 'masculino' ou 'feminino'
while sexo not in 'MmFf':
    sexo = str(input('Dado inválido! Por favor, informe o sexo [M/F]: '))
print('Sexo {} registrado com sucesso.'.format(sexo))
    