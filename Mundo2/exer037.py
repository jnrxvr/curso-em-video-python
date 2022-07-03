n = int(input('Digite um número inteiro para conversão: '))
tipoConversao = int(input('Opções de conversão: '
                      '\n[1] - converter para binário. '
                      '\n[2] - converter para octadecimal'
                      '\n[3] - converter para hexadecimal'
                      '\nSelecione a conversão desejada: '))

if tipoConversao == 1:
    print('--------------------------------------')
    print('O número {} convertido para binário é igual a: {}.' .format(n, bin(n)[2:]))
# [2:] fatiando os dois primeiros dígito para que não apareça as letras '0b'
# pois não é relevante, é só a identificação de binário no python

elif tipoConversao == 2:
    print('--------------------------------------')
    print('O número {} convertido para octal é igual a: {}.' .format(n, oct(n)[2:]))
# [2:] fatiando os dois primeiros dígitos para que não apareça as letras '0o'
# pois não é relevante, é só a identificação de octal no python

elif tipoConversao == 3:
    print('--------------------------------------')
    print('O número {} convertido para hexadecimal é igual a: {}.'.format(n, hex(n)[2:]))
# [2:] fatiando os dois primeiros dígito para que não apareça as letras '0x'
# pois não é relevante, é só a identificação de hexadecimal no python

else:
    print('Opção inválida! Tente novamente.')
