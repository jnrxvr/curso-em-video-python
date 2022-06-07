# crie um programa que leia quantos reais uma pessoa tenha na carteira e moestre quantos doláres ela pode comprar
# US$ 1.00 = R$ 4.80

r = float(input('Digite quantos reais você tem na carteira: '))
conv = r/4.80

print('Com {} reais vocês pode comprar {:.2f} dólares.'.format(r, conv))
