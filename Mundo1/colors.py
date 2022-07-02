# \033[4;30;43m é um código de cor
# ver tabela ansi python para mais cores e mais códigos
# \033[ --> inicia o código
# 4 --> corresponde ao style e possui 4 opções [0, 1, 4, 7]
# 30 --> corresponde a cor do texto e vai de 30 até 37
# 43 --> corresponde a cor do background (fundo) e vai de 40 até 47
# m --> corresponde ao fim do código

print('\033[4;30;43mOlá, Terráqueos!')
# para que a barra de cor fique limitada apenas ao texto, basta colocar um \033[m ao final do texto
print('\033[4;30;43mOlá, Terráqueos! \033[m')
# outra maneira de fazer é através do método format

nome = 'Junior'
# sem formatação de cor no format
print('Olá! É um prazer te conhecer, {}!! ' .format(nome))
# com formatação de cor no format
print('Olá! É um prazer te conhecer, {}{}{}!! ' .format('\033[0;31;40m', nome, '\033[m'))

