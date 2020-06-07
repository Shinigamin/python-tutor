import pygame
from time import sleep
for contagem in range(10, -1, -1):
    sleep(1)
    print(contagem)
print('Bow!! POw! Catapinbas!!')
pygame.init()
pygame.mixer.music.load('Astronomia.mp3')
pygame.mixer.music.play()
pygame.event.wait()