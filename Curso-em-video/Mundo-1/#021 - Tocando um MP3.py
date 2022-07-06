import pygame

# Inserir diretório do arquivo
pygame.init()
pygame.mixer.music.load(
    'enemy.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
