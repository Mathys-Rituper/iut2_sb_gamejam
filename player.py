import pygame
from field import cropspot

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        ### STATISTIQUES INGAME
        self.velocity = 5
        self.max_health = 100
        self.max_health = 100
        self.attack_speed = 1       # coefficient multiplicateur vitesse attaque
        self.attack_strength = 1    # coefficient mulitiplicateur degats
        self.resistance = 0         #pourcentage de degats reduits

        ###INVENTORY
        self.veg_inv = {"P": {"name": "Potato", "amount": 0},
              "W": {"name": "Watermelon", "amount": 0},
              "C": {"name": "carrot", "amount": 0},
              "S": {"name": "Strawberry", "amount": 0},
              "N": {"name": "No Crop", "amount": 0}}
        ###SPRITE
        self.image = pygame.image.load("assets/crop-carrot-3.png") #TODO ajouter le sprite par defaut
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


    def has_no_vegs(self):
        isempty = True
        for key in self.veg_inv.keys():
            if self.veg_inv[key]["amount"] != 0:
                isempty = False
        return isempty

    def dec_veg(self,crop):
        self.veg_inv[crop]["amount"]-=1