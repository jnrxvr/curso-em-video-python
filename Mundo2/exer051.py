# Exercício Python 51:
# Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.
# an = a1 + (n-1) * r

pTermo = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite o valor da razão da P.A: '))
decimoTermo = pTermo + (10 - 1) * r     # cálculo do décimo termo

# (décimoTermo + razao) equivale ao 11ª termo que será excludente, faz-se isso para que sejam mostrados os 10º termos
for i in range(pTermo, decimoTermo + r, r):     # passo aqui é a prórpia razão aritmética
    print(i, end=' ')