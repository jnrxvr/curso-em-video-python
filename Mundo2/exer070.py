# Exercício Python 70:
# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

totalCompra = 0
precoProduto = 0
maisQueMil = 0
cont = 0
menorPreco = 0
resp = ''

while True:
    nomeProduto = input('Digite o nome do produto: ')
    precoProduto = float(input('Digite o valor do produto: R$ '))

    resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while resp != 'S' and resp != 's' and resp != 'N' and resp != 'n':
        print('Resposta inválida! Digite S/s ou N/n.')
        resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]

    totalCompra += precoProduto

    if precoProduto > 1000:
        maisQueMil += 1

    cont += 1

    if cont == 1:
        menorPreco = precoProduto
        nome = nomeProduto
    else:
        if precoProduto < menorPreco:
            menorPreco = precoProduto
            nome = nomeProduto

    if resp == 'n':
        break

print('-' * 35)
print(f'Total gasto: R$ {totalCompra}.'
          f'\nTotal de produtos que custam mais de R$ 1000: {maisQueMil} produto(s).'
          f'\nProduto mais barato: {nome}')
