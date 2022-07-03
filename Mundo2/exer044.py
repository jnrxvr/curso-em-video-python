# Exercício Python 044:
# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

valorCompra = float(input('Digite o valor a ser pago: '))
formaPagamento = int(input('Escolha a forma de pagamento: '
                           '\n[1] - à vista dinheiro/cheque (com 10% de desconto)'
                           '\n[2] - à vista no cartão (com 5% de desconto)'
                           '\n[3] - em 2x no cartão (sem juros)'
                           '\n[4] - em 3x ou mais no cartão (com juros).'
                           '\nOpção selecionada: '))
numParcelas = 0

if formaPagamento == 1:
    print('-------------------------------------------------------------------')
    print('Forma de pagamento escolhida: à vista em dinheiro ou cheque com 10% de desconto. ')
    print('Sua compra de R$ {:.2f} com 10% de desconto, será de R$ {:.2f}.'. format(valorCompra, (valorCompra  * 0.9)))
elif formaPagamento == 2:
    print('-------------------------------------------------------------------')
    print('Forma de pagamento escolhida: à vista no cartão com 5% de desconto. ')
    print('Sua compra de R$ {:.2f} com 5% de desconto, será de R$ {:.2f}.'.format(valorCompra, (valorCompra * 0.95)))
elif formaPagamento == 3:
    print('-------------------------------------------------------------------')
    print('Forma de pagamento escolhida: 2x no cartão sem juros. ')
    print('Compra de R$ {:.2f} dividida em 2x de R$ {:.2f}.'.format(valorCompra, (valorCompra/2)))
elif formaPagamento == 4:
    numParcelas = int(input('Digite o número de parcelas desejado (3x até 10x): '))
    print('-------------------------------------------------------------------')
    print('Forma de pagamento escolhida: {}x no cartão com juros. '. format(numParcelas))
    print('Compra de R$ {:.2f} dividida em {} parcelas de R$ {:.2f}. '
          '\nValor final de R$ {:.2f}.'.format(valorCompra, numParcelas, ((valorCompra * 1.2) / numParcelas), (valorCompra * 1.2)))
else:
    print('-------------------------------------------------------------------')
    print('Opção inválida! Por favor selecione opções de 1 a 4.')


