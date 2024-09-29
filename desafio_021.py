# Faça um programa que abra e reproduza o áudio de um arquivo MP3

import pygame


pygame.init()
pygame.mixer.music.load('desafio_021.mp3')
pygame.mixer.music.play()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.mixer.music.stop()
pygame.quit()