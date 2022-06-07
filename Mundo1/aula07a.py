nome = input('Qual o seu nome? ')
print('Prazer em te conhecer, {}.'.format(nome))

# insere o texto em 20 caracteres
print('Prazer em te conhecer, {:20}.'.format(nome))

# insere o texto em 20 caracteres e o alinha à direita
print('Prazer em te conhecer, {:>20}.'.format(nome))

# insere o texto em 20 caracteres e o alinha à esquerda
print('Prazer em te conhecer, {:<20}.'.format(nome))

# insere o texto em 20 caracteres e o alinha de forma centralizada
print('Prazer em te conhecer, {:^20}.'.format(nome))

# insere o texto em 20 carac, o centraliza e insere o símbolo de igual (serve qq símbolo) antes e após a variável
print('Prazer em te conhecer, {:=^20}.'.format(nome))