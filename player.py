import pygame

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

        ###SPRITE
        self.image = pygame.image.load("") #TODO ajouter le sprite par defaut
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
