import pygame
from cropfield import cropspot

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super.__init__()

        ### STATISTIQUES INGAME
        self.velocity = 5
        self.max_health = 100
        self.max_health = 100
        self.attack_speed = 1       # coefficient multiplicateur vitesse attaque
        self.attack_strength = 1    # coefficient mulitiplicateur degats
        self.resistance = 0         #pourcentage de degats reduits

        ###INVENTORY
        self.veg_inv = {x : {"name" :cropspot.crop_types[x]["name"], "amount" : 0} for x in cropspot.crop_types.keys}
        ###SPRITE
        self.image = pygame.image.load("") #TODO ajouter le sprite par defaut
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y


    def has_no_vegs(self):
        isempty = True
        for key in self.veg_inv.keys():
            if self.veg_inv[key]["amount"] != 0:
                isempty = False
        return isempty