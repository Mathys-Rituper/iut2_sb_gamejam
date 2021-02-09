import pygame
import animation
from projectile import Projectile

class Player(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__("player")

        ### STATISTIQUES INGAME
        self.velocity = 5
        self.health = 100
        self.max_health = 100
        self.attack_speed = 1       # coefficient multiplicateur vitesse attaque
        self.attack_strength = 1    # coefficient mulitiplicateur degats
        self.resistance = 0         #pourcentage de degats reduits
        self.elapse = 0
        self.game = game
        self.all_projectiles = pygame.sprite.Group()
        ###INVENTORY
        self.veg_inv = {"P": {"name": "Potato", "amount": 1},
                        "W": {"name": "Watermelon", "amount": 0},
                        "C": {"name": "carrot", "amount": 5},
                        "S": {"name": "Strawberry", "amount": 0},
                        "N": {"name": "No Crop", "amount": 0}}

        ###SPRITE

        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        self.rect.y = 500
        self.rect2 = self.image.get_rect()

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        self.current_orientation = "right"
        if not self.game.collision(self, self.game.wall):
            self.rect.x += self.velocity
        self.update()

    def move_left(self):
        self.current_orientation = "left"
        self.rect.x -= self.velocity
        self.update()

    def move_up(self):
        self.current_orientation = "up"
        self.rect.y -= self.velocity
        self.update()

    def move_down(self):
        self.current_orientation = "down"
        self.rect.y += self.velocity
        self.update()

    def has_no_vegs(self):
        isempty = True
        for key in self.veg_inv.keys():
            if self.veg_inv[key]["amount"] != 0:
                isempty = False
        return isempty

    def dec_veg(self,crop):
        self.veg_inv[crop]["amount"]-=1

    def update(self):

        if pygame.time.get_ticks() - self.elapse> 100:
            self.animate()
            self.elapse = pygame.time.get_ticks()
