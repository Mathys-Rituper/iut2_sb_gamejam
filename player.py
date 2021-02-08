import pygame
import animation

class Player(animation.AnimateSprite):
    def __init__(self):
        super().__init__("player")

        ### STATISTIQUES INGAME
        self.velocity = 1
        self.health = 100
        self.max_health = 100
        self.attack_speed = 1       # coefficient multiplicateur vitesse attaque
        self.attack_strength = 1    # coefficient mulitiplicateur degats
        self.resistance = 0         #pourcentage de degats reduits

        ###SPRITE

        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y



    def move_right(self):
        self.current_orientation = "right"
        self.rect.x += self.velocity
        self.animate()

    def move_left(self):
        self.current_orientation = "left"
        self.rect.x -= self.velocity
        self.animate()

    def move_up(self):
        self.current_orientation = "up"
        self.rect.y -= self.velocity
        self.animate()

    def move_down(self):
        self.current_orientation = "down"
        self.rect.y += self.velocity
        self.animate()


