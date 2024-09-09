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
    def __init__(self, x, y, index, height):
        colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
        color = choice(colors)
        super().__init__()
        self.image = pygame.Surface((23, height))
        self.image.fill(color)
        self.index = index
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

    def update2(self):
        for layer in layers:
            if layer == bottom_liquids:
                last_layer = layer
            if self in layer:
                self.rect.midbottom = last_layer.sprites()[self.index].rect.midtop
                last_layer = layer

    def update(self):
        if self in bottom_liquids:
            self.rect.midbottom = tubes.sprites()[self.index].rect.midbottom
        elif self in mid_bottom_liquids:
            self.rect.midbottom = bottom_liquids.sprites()[self.index].rect.midtop
        elif self in top_bottom_liquids:
            self.rect.midbottom = mid_bottom_liquids.sprites()[self.index].rect.midtop
        elif self in bottom_top_liquids:
            self.rect.midbottom = top_bottom_liquids.sprites()[self.index].rect.midtop
        elif self in mid_top_liquids:
            self.rect.midbottom = bottom_top_liquids.sprites()[self.index].rect.midtop
        elif self in top_liquids:
            self.rect.midbottom = mid_top_liquids.sprites()[self.index].rect.midtop


class Tube(pygame.sprite.Sprite):

    def __init__(self, x, y, index):
        super().__init__()
        self.image, self.rect = load_image("tube.png", -1, 2)
        self.index = index
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.selected = False
        self.fill_tube(self.x, self.y, self.index, (self.rect.height / 6) - 1)

    def fill_tube(self, x, y, index, height):

        for layer in layers:
            liquid = Liquid(x, y, index, height)
            layer.add(liquid)

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


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True


tubes = pygame.sprite.Group()
bottom_liquids = pygame.sprite.Group()
mid_bottom_liquids = pygame.sprite.Group()
top_bottom_liquids = pygame.sprite.Group()
bottom_top_liquids = pygame.sprite.Group()
mid_top_liquids = pygame.sprite.Group()
top_liquids = pygame.sprite.Group()

layers = [
    bottom_liquids,
    mid_bottom_liquids,
    top_bottom_liquids,
    bottom_top_liquids,
    mid_top_liquids,
    top_liquids,
]

create_tubes(4, 2)

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
