# dado um número determine se ele é primo ou não é primo

n = int(input("Digite um número: "))
i = 1
ehPrimo = 0
naoEhPrimo = 0

while i <= n:
    if n % i == 0:
       # print("É divisível por: {}" .format(i))
        ehPrimo += 1
        i = i + 1
    else:
       # print("Não é divisível por: {}" .format(i))
        naoEhPrimo += 1
        i = i + 1
if ehPrimo == 2:
    print("primo")
else:
    print("não primo")
