# Exercício Python 36:
# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e
# em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou
# então o empréstimo será negado.

valorCasa = float(input('Digite o valor do imóvel: '))
salarioComprador = float(input('Digite o seu salário mensal: '))
anosAPagar = int(input('Digite em quantos anos pretende quitar o empréstimo: '))
tempoEmprestimo = anosAPagar * 12
prestacaoMensal = valorCasa / tempoEmprestimo

if salarioComprador * 0.3 > (valorCasa/tempoEmprestimo):
    print('--------------------------------------')
    print('Parabéns! Seu empréstimo foi aprovado.')
    print('--------------------------------------')
    print('Seu imóvel no valor de R$ {:.2F}, com financiamento de {} anos.' .format(valorCasa, anosAPagar))
    print('Sua prestação será de R$ {:.3f} por mês.'.format(prestacaoMensal))
    print('--------------------------------------')

# como a aula abordava elif, usei elif para fixar o conteúdo
# mas não havia necessidade, um if/else já resolveria
elif salarioComprador * 0.3 <= (valorCasa/tempoEmprestimo):
    print('--------------------------------------')
    print('Lamentamos muito! Seu empréstimo não foi aprovado. :(')