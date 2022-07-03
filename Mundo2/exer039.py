# Exercício Python 39:
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoNascimento = int(input('Digite o ano de nascimento: '))
print('********************************************')
anoAtual = date.today().year
print('Quem nasceu em {} tem {} anos em {}.' .format(anoNascimento, (anoAtual - anoNascimento), anoAtual))
idade = 0
anoAlistamento = 0

if (anoAtual - anoNascimento) == 18:
    print('É hora de se alistar!')

elif (anoAtual - anoNascimento) > 18:
    idade = anoAtual - anoNascimento
    anoAlistamento = anoAtual - (idade - 18)
    print('Seu tempo de alistamente já passou!')
    print('Seu ano de alistamento foi {}.' .format(anoAlistamento))
else:
    idade = anoAtual - anoNascimento
    anoAlistamento = anoAtual + (18 - idade)
    print('Ainda falta(m) {} ano(s) para o seu alistamento!' .format(18 - idade))
    print('Seu alistamento será apenas em {}.!' .format(anoAlistamento))


