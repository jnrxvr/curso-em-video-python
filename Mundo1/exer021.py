import pygame
pygame.init() # iniciando o uso da biblioteca

# o arquivo MP3 (ex021.mp3) deve estar contido na mesma pasta de trabalho
pygame.mixer.music.load('ex021.mp3') # como não a esse arquivo, não funcionará corretamente

pygame.mixer.music.play() # toca a música
pygame.event.wait() # espera o término da música para encerrar o programa
