# escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros

medida = float(input('Digite o valor em metro(s) que deseja converter para centímetro(s): '))
print('O valor de {} metro(s) convertido para centímetro(s) é de {} cm.'.format(medida, medida * 100))
print('O valor de {} metro(s) convertido para milimetro(s) é de {} mm.'.format(medida, medida * 1000))