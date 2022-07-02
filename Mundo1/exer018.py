import math

ang = float(input('Digite o valor de um ângulo: '))

# o ângulo foi dado em graus, mas o método só calcula com ângulos em radianos
# usa-se 'math.radians' para converter para radianos

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O seno do ângulo {} é {:.2f}.' .format(ang, sen))
print('O cosseno do ângulo {} é {:.2f}.' .format(ang, cos))
print('A tangente do ângulo {} é {:.2f}.' .format(ang, tan))
