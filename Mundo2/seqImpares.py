# Receba um número inteiro positivo na entrada e
# imprima os 'N' primeiros números ímpares naturais.
# Para a saída, siga o formato do exemplo abaixo.

n = int(input("Digite um número inteiro positivo: "))

i = -1

while n != 0:
    i += 2
    n -= 1
    print(i)
