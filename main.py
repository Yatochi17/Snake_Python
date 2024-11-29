import pygame
import sys
import random

from pygame.examples.go_over_there import screen, clock

pygame.init()

SW, SH = 800, 800

FONT = pygame.font.Font("Arial", 100)

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Snake!")
clock = pygame.time.clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(10)