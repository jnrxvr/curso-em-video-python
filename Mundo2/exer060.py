# exercicio 60
# calcule o fatorial de um numero qualquer

n = int(input("Digite um número para cálculo do fatorial: "))
fat = 1


if n == 0:
    1
else:
    while n != 0:
        fat = fat * n
        n -= 1
print('***********************')
print('O fatorial é {}.' .format(fat))
