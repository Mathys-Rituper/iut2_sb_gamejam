import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super.__init__()
        self.velocity = 5
        self.max_health = 100
        self.max_health = 100