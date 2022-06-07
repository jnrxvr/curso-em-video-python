# leia a largura em metros e a altura em metros de uma parede e calcule sua área e a qtd de tinta necessária para pintá-la
# sabendo que 1L de tinta pinta 2m²

a = float(input('Digite a altura em metros da parede: '))
l = float(input('Digite a largura em metros da parede: '))
area = a * l
print('A área da parede é de {:.2f}m², portanto gastará {:.2f} litros de tinta.'.format(area, area/2))