# Exercício Python 53: Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()        # separando a frase em as palavras
junto = ''.join(palavras)       # juntando as palavras separadas sem os espaços
inverso = ''                    # invertendo a frase (string)

# len(junto) - 1 (tamanho total da string menos 1 pois começa com índice 0
# -1 pois o último digito de trás pra frente é o 0 (zero), e seria excludente, para incluí-lo tem que ir até -1
# -1 passo negativo pois queremos ir de trás pra frente

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if junto == inverso:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase NÃO é um palíndromo!')

# OUTRA FORMA DE SER FEITO SEM O FOR


