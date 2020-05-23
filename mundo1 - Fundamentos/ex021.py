import pygame

m = ''' (DESAFIO 021)
    Faça um programa em Python que abra e 
    reproduza o áudio de um de arquivo MP3: '''
print(m, '\n')

pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
