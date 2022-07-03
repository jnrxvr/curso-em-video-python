# Exercício Python 040:
# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2
print('-----------------------------------------------------')
print('Com as notas {} e {}, o(a) aluno(a) tem média {}. ' .format(nota1, nota2, media))


if media < 5:
    print('ALUNO REPROVADO!')
elif 5.0 <= media <= 6.9: # simplificando a condição ( media > 5.0 and media < 6.9 )
    print('ALUNO EM RECUPERAÇÃO!')
else:
    print('ALUNO APROVADO!')
