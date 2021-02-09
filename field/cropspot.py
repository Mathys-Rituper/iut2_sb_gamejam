import pygame
import random

crop_types = {"P": {"name": "Potato", "sprite_path": "assets/potato/"},
              "W": {"name": "Watermelon", "sprite_path": "assets/watermelon/"},
              "C": {"name": "carrot", "sprite_path": "assets/carrot/"},
              "S": {"name": "Strawberry", "sprite_path": "assets/strawberry/"},
              "N": {"name": "No Crop", "sprite_path": "assets/no_crop/"}}


class Cropspot(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.crop_type = crop_types["N"]  # Par défaut la case de culture est vide
        self.image = pygame.image.load("assets/no_crop/0.png")
        self.maturation = 0  # Niveaux de maturation possible : 0 (vient d'être planté), 1 (une nuit est déjà
        # passée), 2 (2 nuits sont passées depuis la plantation et on peut récolter le résultat)


    def new_culture(self, crop):
        self.crop_type = crop_types[crop]
        self.maturation = 0
        self.image = pygame.image.load(self.crop_type["sprite_path"] + str(self.maturation) + ".png")

    def recolte(self):
        resultat_recolte = 0  # par défaut à 0; si la plantation n'est pas mure
        if self.maturation == 2:
            resultat_recolte = random.randint(3, 5)  # Valeurs arbitraires à équilibrer
            self.new_culture("N")
        return resultat_recolte

    def is_empty(self):
        return self.crop_type==crop_types["N"]

    def get_crop_name(self):
        return crop_types[self.crop_type]["name"]