# Exercício Python 72:
# Crie um programa que tenha uma tupla totalmente preenchida
# com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado
# (entre 0 e 20) e mostrá-lo por extenso.
# pergunte se o usuario deseja continuar ou não

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
           'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze',
           'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    n = int(input('Digite um número de 0 a 20: '))
    while True:
        if 0 <= n <= 20:
            print(numeros[n])
            break
        else:
            print('Número inválido! Tente novamente.')
            n = int(input('Digite um número de 0 a 20: '))

    resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    while resp != 'S' and resp != 's' and resp != 'N' and resp != 'n':
        print('Resposta inválida! Digite S/s ou N/n.')
        resp = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]

    if resp == 'n':
        break
