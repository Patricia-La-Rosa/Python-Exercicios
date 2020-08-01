import pygame
# deve se instalar a biblioteca pygame e iniciar
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()

