# tuplas são imutáveis, podendo ser alteradas apenas quando o prog não esta sendo executado
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batataa Frita')

# se eu não precisar saber a posição no print
for comida in lanche:
    print(f'Eu vou comer {comida}.')

#  caso eu necessite saber a posição no print
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')     # lanche[cont]: lanche na posição do contador

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')

# para ordenar uma tupla (não altera a tupla, pois ela é imutável)

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batataa Frita')
print(sorted(lanche))

a = (2, 5, 7)
b = (7, 9, 2, 5)
c = a + b # CONCATENAÇÃO DE TUPLAS (não é uma soma de elementos por elementos)
# (a + b) é diferente de (b + a) em tuplas
print(a)
print(b)
print(c)

print(c.count(7))       # conta quantas vezes o número 7 aparece na tupla
print(c.index(9))       # mostra o índice/posição do elemento indicado

pessoa = ('Junior', 28, 'Masculino', 105.90)        # as tuplas podem conter elementos de tipos diferentes
del(pessoa) # EXCLUI A TUPLA INTEIRA DA MEMÓRIA