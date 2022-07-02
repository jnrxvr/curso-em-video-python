# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
# considere apenas dias inteiros

km  = float(input('Digite a quantidade de Km percorridos: '))
dias = int(input('Digite a quantidade de dias alugados: '))

preco_total = (60 * dias) + (km * 0.15)
print('O valor total a pagar pelo aluguel do carro por {} dia(s) e por {} Km(s) rodados é de {} reais.'.format(dias, km, preco_total))