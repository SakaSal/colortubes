import pygame


class Tube(pygame.sprite.Sprite):
    # this is a test note.

    def __init__(self, x, y, index, fill=6):
        super().__init__()
        self.image, self.rect = load_image("tube.png", -1, 2)
        self.index = index
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.selected = False
        self.fill = fill
        self.fill_tube(
            self.x, self.y, self.index, (self.rect.height / 6) - 1, self.fill
        )

    def fill_tube(self, x, y, index, height, fill):
        for layer in layers[0:fill]:
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
