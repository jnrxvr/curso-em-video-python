# Exercício Python 62: Melhore o DESAFIO 61,
# perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('GERADOR DE PA')
primeiro = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite o valor da razão da P.A: '))
termo = primeiro
cont = 1
total = 0
mais = 10   # esse exercício começa com o prog mostrando 10 termos

while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' ')
        termo += razao
        cont += 1
    mais = int(input('\nQuantos termos você quer a mais? '))

print('Progressão finalizada com {} termos mostrados.'.format(total))
