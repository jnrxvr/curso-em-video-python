# Exercício Python 071:
# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

resp = ''
saque = 0

saque = int(input('Digite o valor que deseja sacar: R$ '))
total = saque
cedulaAtual = 50        # nesse caso a cédula máx é a de 50
totCedulas = 0

print('-' * 35)
while True:
    if total >= cedulaAtual:
        total -= cedulaAtual
        totCedulas += 1
    else:
        if totCedulas > 0:
            print(f'Total de {totCedulas} cédulas de R$ {cedulaAtual}')
        if cedulaAtual == 50:
            cedulaAtual = 20
        elif cedulaAtual == 20:
            cedulaAtual = 10
        elif cedulaAtual == 10:
            cedulaAtual = 1
        totCedulas = 0
        if total == 0:
            break
print('-' * 35)