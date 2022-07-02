# Exercício Python 29: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Digite a velocidade do carro: '))
multa = (vel - 80) * 7

if vel > 80:
    print('Você foi multado!')
    print('Sua multa custará {} reais.' .format(multa))

print('Tenha um bom dia! Dirija com segurança.') # 'vel <= 80' não entra na condição e executa direto o print