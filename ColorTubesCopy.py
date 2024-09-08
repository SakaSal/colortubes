# Example file showing a basic pygame "game loop"
import os
import pygame
from random import choice
from pygame.sprite import Group

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "assets")
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 200
holding = False


def load_image(name, colorkey=None, scale=1):
    fullname = os.path.join(data_dir, name)
    image = pygame.image.load(fullname).convert_alpha()
    image = pygame.transform.scale_by(image, scale)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()


class Liquid(pygame.sprite.Sprite):
    def __init__(self, x, y, index):
        colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
        color = choice(colors)
        super().__init__()
        self.image = pygame.Surface((23, 15))
        self.image.fill(color)
        self.index = index
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Tube(pygame.sprite.Sprite):

    def __init__(self, x, y, index):
        super().__init__()
        self.image, self.rect = load_image("tube.png", -1, 2)
        self.index = index
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.selected = False
        self.fill_tube(self.x, self.y, self.index)

        # self.fill_tube()

    def fill_tube(self, x, y, index):
        liquid = Liquid(x, y + 22, index)
        bottom_liquids.add(liquid)

    def re__init__(self, x, y):
        self.rect.center = (x, y)
        self.selected = False

    def input(self):
        global holding
        pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_just_pressed()
        if not holding:
            if mouse[0] and self.rect.collidepoint(pos):
                self.selected = True
                holding = True
        if self.selected:
            self.rect.center = pos
            if mouse[2]:
                self.re__init__(self.x, self.y)
                holding = False

    def update(self):
        bottom_liquids.sprites()[self.index].rect.midbottom = self.rect.midbottom
        self.input()


def create_tubes(rows, columns):
    index = 0
    w_interval = SCREEN_WIDTH / rows
    w_start = w_interval - (w_interval / 2)
    c_interval = SCREEN_HEIGHT / columns
    c_start = c_interval / 2
    for col in range(columns):
        for row in range(rows):
            tube = Tube(w_start, c_start, index)
            w_start += w_interval
            tubes.add(tube)
            index += 1
        w_start = w_interval - (w_interval / 2)
        c_start += c_interval


# pygame setup

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True


tubes = pygame.sprite.Group()
bottom_liquids = pygame.sprite.Group()
create_tubes(4, 2)
print(tubes.sprites()[4].rect.center)


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
    bottom_liquids.update()
    tubes.update()
    bottom_liquids.draw(screen)
    tubes.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
