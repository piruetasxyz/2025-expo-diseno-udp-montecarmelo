import vlc

import sys
import os

import pygame
import pygame.freetype


pygame.init()

pygame.display.set_caption('hello world')

screen = pygame.display.set_mode((800, 600), 0, 32)

font = pygame.freetype.SysFont('Arial', 24)

title = font.render('sup', False, (250, 250, 250))

running = True

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                   
    screen.fill((25, 25, 25))
    screen.blit(title, (0, 0))
    pygame.display.update()

pygame.quit()

