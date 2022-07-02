from math import hypot

catOp = float(input('Digite o valor do cateto oposto: '))
catAd = float(input('Digite o valor do cateto adjacente: '))
hipo = hypot(catAd, catOp)

print('O comprimento da hipotenusa é de {} cm.' .format(hipo))
