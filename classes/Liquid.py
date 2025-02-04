import pygame


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
