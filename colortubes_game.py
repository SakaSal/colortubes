import os
from random import choice
from classes import Tube, Liquid
from functions import functions
from settings import settings

import pygame


pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True


tubes = pygame.sprite.Group()
bottom_liquids = pygame.sprite.Group()
mid_bottom_liquids = pygame.sprite.Group()
top_bottom_liquids = pygame.sprite.Group()
bottom_top_liquids = pygame.sprite.Group()
mid_top_liquids = pygame.sprite.Group()
top_liquids = pygame.sprite.Group()

layers = (
    bottom_liquids,
    mid_bottom_liquids,
    top_bottom_liquids,
    bottom_top_liquids,
    mid_top_liquids,
    top_liquids,
)


functions.create_tubes(4, 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")
    # RENDER YOUR GAME HERE
    # update and draw tubes group
    for item in layers:
        item.update()
    tubes.update()
    for item in layers:
        item.draw(screen)
    tubes.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
pygame.quit()
