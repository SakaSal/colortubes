import pygame
from settings import settings


def load_image(name, colorkey=None, scale=1):
    fullname = settings.os.path.join(data_dir, name)
    image = pygame.image.load(fullname).convert_alpha()
    image = pygame.transform.scale_by(image, scale)

    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()


def create_tubes(rows, columns):
    index = 0
    w_interval = settings.SCREEN_WIDTH / rows
    w_start = w_interval - (w_interval / 2)
    c_interval = settings.SCREEN_HEIGHT / columns
    c_start = c_interval / 2
    for col in range(columns):
        for row in range(rows):
            tube = Tube.Tube(w_start, c_start, index)
            w_start += w_interval
            tubes.add(tube)
            index += 1
        w_start = w_interval - (w_interval / 2)
        c_start += c_interval
