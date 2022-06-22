import pygame # a library for gaming development

pygame.init()
pygame.mixer.music.load('queen.mp3')
pygame.mixer.music.play()

input('press Enter to stop: ')

pygame.mixer.music.stop()
