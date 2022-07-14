# Exercício Python 53: Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.

# OUTRA FORMA DE SER FEITO SEM USAR O LAÇO FOR

frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()        # separando a frase em as palavras
junto = ''.join(palavras)       # juntando as palavras separadas sem os espaços
inverso = junto[::-1]           # invertendo a frase (string)
print('O inverso de {} é {}.'.format(junto, inverso))

if junto == inverso:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase NÃO é um palíndromo!')