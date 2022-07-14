# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
soma = 0
mult = 0
maior = 0
novo_num = 0
opcao = int(input('Selecione uma opção:'
          '\n[ 1 ] somar'
          '\n[ 2 ] multiplicar'
          '\n[ 3 ] maior'
          '\n[ 4 ] novos números'
          '\n[ 5 ] sair'
          '\nOpção selecionada: '))
print('*******************************')

while opcao != 5:
    if opcao == 1:
        soma = n1 + n2
        print('A soma de {} e {} é {}.'.format(n1, n2, soma))
        print('*******************************')
        opcao = int(input('Selecione uma opção:'
                          '\n[ 1 ] somar'
                          '\n[ 2 ] multiplicar'
                          '\n[ 3 ] maior'
                          '\n[ 4 ] novos números'
                          '\n[ 5 ] sair'
                          '\nOpção selecionada: '))
        print('*******************************')
    elif opcao == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, mult))
        print('*******************************')
        opcao = int(input('Selecione uma opção:'
                          '\n[ 1 ] somar'
                          '\n[ 2 ] multiplicar'
                          '\n[ 3 ] maior'
                          '\n[ 4 ] novos números'
                          '\n[ 5 ] sair'
                          '\nOpção selecionada: '))
        print('*******************************')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('O maior número entre {} e {} é {}.'.format(n1, n2, maior))
            print('*******************************')
            opcao = int(input('Selecione uma opção:'
                              '\n[ 1 ] somar'
                              '\n[ 2 ] multiplicar'
                              '\n[ 3 ] maior'
                              '\n[ 4 ] novos números'
                              '\n[ 5 ] sair'
                              '\nOpção selecionada: '))
            print('*******************************')
        elif n2 > n1:
            maior = n2
            print('O maior número entre {} e {} é {}.'.format(n1, n2, maior))
            print('*******************************')
            opcao = int(input('Selecione uma opção:'
                              '\n[ 1 ] somar'
                              '\n[ 2 ] multiplicar'
                              '\n[ 3 ] maior'
                              '\n[ 4 ] novos números'
                              '\n[ 5 ] sair'
                              '\nOpção selecionada: '))
            print('*******************************')
        else:
            print('Os números digitados são iguais! Tente novos valores.')
            print('*******************************')
            opcao = int(input('Selecione uma opção:'
                              '\n[ 1 ] somar'
                              '\n[ 2 ] multiplicar'
                              '\n[ 3 ] maior'
                              '\n[ 4 ] novos números'
                              '\n[ 5 ] sair'
                              '\nOpção selecionada: '))
            print('*******************************')
    elif opcao == 4:
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
        print('*******************************')
        opcao = int(input('Selecione uma opção:'
                          '\n[ 1 ] somar'
                          '\n[ 2 ] multiplicar'
                          '\n[ 3 ] maior'
                          '\n[ 4 ] novos números'
                          '\n[ 5 ] sair'
                          '\nOpção selecionada: '))
        print('*******************************')
    elif (opcao < 1) or (opcao > 5):
        print('Opção inválida! Selecione uma das 5 opções.')
        print('*******************************')
        opcao = int(input('Selecione uma opção:'
                          '\n[ 1 ] somar'
                          '\n[ 2 ] multiplicar'
                          '\n[ 3 ] maior'
                          '\n[ 4 ] novos números'
                          '\n[ 5 ] sair'
                          '\nOpção selecionada: '))
        print('*******************************')
