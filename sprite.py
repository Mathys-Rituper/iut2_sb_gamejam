import pygame
from setting import *
from tile_map import TileMap


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, till, x, y, w, h):
        self.groups = till.wall
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.rect = pygame.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
