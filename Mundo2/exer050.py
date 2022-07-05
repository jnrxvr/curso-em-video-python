# Exercício Python 50:
# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
# extra: conte o número de pares digitados

# não pode ser range(1,6), pois o laço sempre executa uma iteração a menos
# como eu quero 6 números preciso colocar 7 para que o laço itere corretamente

soma = 0    # acumulador
n = 0

for i in range(1, 7):   # 7 é excludente, portanto o laço vai até 6
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        soma += num
        n += 1
print('******************************')
print('Número de pares digitados: {}.'
      '\nA soma dos números pares é: {}.' . format(n, soma))
