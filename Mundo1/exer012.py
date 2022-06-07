# leio o preço de um produto e mostre o novo preço com desconto de 5%

preco = float(input('Digite o preço do produto: '))
preco_com_desc = preco-(preco * 0.05)
print('O valor do produto com 5% de desconto é de {:.2f} reais.'.format(preco_com_desc))