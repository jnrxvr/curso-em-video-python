# Exercício Python 73:
# Crie uma tupla preenchida com os 20 primeiros
# colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time do Flamengo.

# tabela série A 2022
serieA = ('Palmeiras', 'Corinthians', 'Atlético-MG', 'Fluminense', 'Atlético-PR',
          'Internacional', 'Flamengo', 'Bragantino', 'Santos', 'São Paulo',
          'Ceará', 'Botafogo', 'Avaí', 'Goiás', 'Cuiabá',
          'Coritiba', 'América-MG', 'Atlético-GO', 'Fortaleza', 'Juventude')

print('*' * 35)
print('Classificação da Série A do Brasileirão 2022')
print(serieA)
print('*' * 35)
print('Os 5 primeiros colocados:')
print(serieA[0:5])
print('*' * 35)
print('Os últimos 4 colocados:')
print(serieA[-4:])      # posição -4 até a posição -1 (seriA[-1:-4] - está incorreto)
print('*' * 35)
print('Times em ordem alfabética:')
print(sorted(serieA))
print('*' * 35)
print('Posição do Flamengo na tabela: {}ª posição.'.format(serieA.index('Flamengo') + 1))
# "+ 1" - para que exiba a posiçao relativa à tabela, não a posição relativa a tupla, pois esta começa em 0
print('*' * 35)
