n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
exp = n1 ** n2
resto = n1 % n2

# \n serve para quebras de linhas
# end='' serve para que não haja quebra de linhas, observe o exemplo abaixo
print('A soma é {}, o produto é {} e a divisão é {:.3f}' .format(s, m, d), end=' ') # com espaço, mas pode-se símbolos também
print('Divisão inteira é {} e a potência é {}' . format(di, exp))

print('A soma é {}, o produto é {} e a divisão é {:.3f}' .format(s, m, d), end=' >>> ') # com espaço e símbolo
print('Divisão inteira é {} e a potência é {}' . format(di, exp))
