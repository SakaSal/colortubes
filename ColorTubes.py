# Example file showing a basic pygame "game loop"
import os
import pygame
from pygame.sprite import Group


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400


class Tube(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/tube.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


tube = Tube(400, 200)


# pygame setup

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

print(__file__[0])
pygame.quit()
