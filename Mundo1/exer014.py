# faça um programa que leia uma temperatura em graus celsius e converta para graus fahrenheit

c = float(input('Digite a temperatura em graus Celsius para conversão: '))
f = c * 1.8 + 32

print('A temperatura de {} °C equivale a  {} °F.'.format(c, f))
