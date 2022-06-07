# faça um programa que leia algo pelo teclado (string, int, float...)
# e mostre # todos os tipos de informações sobre ele

x = input('Digite alguma coisa para verificar seus tipo e outras informações: ')
print('O tipo primitivo desse valor é: ', type(x))
print('Esse valor é alphanumérico?', x.isalnum())
print('Esse valor só contém números?', x.isnumeric())
print('Esse valor só contém letras?', x.isalpha())
print('Esse valor está todo em minúsculo?', x.islower())
print('Esse valor está todo em maiúsculo', x.isupper())
print('Esse valor contém apenas espaços?', x.isspace())
print('Esse valor está capitalizado?', x.istitle())


